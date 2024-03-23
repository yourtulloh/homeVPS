try:
    import os
    import psutil
    import httpx
    import shutil
    import subprocess
except ImportError:
    import subprocess
    import sys
    print("Some modules are missing. Installing them now...")
    try:
        subprocess.run(["pip3", "install", "--no-cache-dir", "psutil", "httpx[http2]"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install required modules: {e}")
        sys.exit(1)
    import os, psutil, shutil, httpx


def humansize(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0


def progress_bar_string(pct):
    pct = float(pct.strip("%"))
    p = min(max(pct, 0), 100)
    cFull = int(p // 9)
    p_str = "■" * cFull
    p_str += "□" * (11 - cFull)
    return f"[{p_str}]"


def cmd_exec(cmd, shell=False):
    if shell:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    else:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode().strip()
    stderr = stderr.decode().strip()
    return stdout, stderr, proc.returncode


def sys():
    zone = None
    with httpx.Client(http2=True, trust_env=True, timeout=httpx.Timeout(5)) as http:
        zone = (http.get("https://ipinfo.io")).json()
    if zone:
        zone = zone.get("timezone")
    pyU = psutil.Process(os.getpid())
    pyU = humansize(pyU.memory_info().rss)
    fetch = (cmd_exec("neofetch --disable memory resolution underline --stdout", True))[0]
    m = psutil.virtual_memory()
    percentage_memory = m.percent
    mused = humansize(m.used)
    mtotal = humansize(m.total)
    mfree = humansize(m.available)
    disk = shutil.disk_usage(".")
    percentage_disk = round((disk.used / disk.total) * 100, 2)
    disktotal = humansize(disk.total)
    diskfree = humansize(disk.free)
    diskused = humansize(disk.used)
    sent = humansize(psutil.net_io_counters().bytes_sent)
    recv = humansize(psutil.net_io_counters().bytes_recv)
    swap = psutil.swap_memory()
    swaptotal = swap.total
    swapused = swap.percent
    swapused = f"{swapused}%" if swapused != float(0) else "Not Set"
    if swaptotal != 0:
        isswap = f"""
SWAP RAM
Total     :  {humansize(swaptotal)}
Used      :  {swapused}
"""
    else:
        isswap = ""
    cpufrq = getattr(psutil.cpu_freq(), "current", None)
    cpufrq = f"{round(cpufrq)} Mhz" if cpufrq is not None else "Disabled"
    rcpu = getattr(psutil, "cpu_count", None)
    if rcpu is not None:
        logic, core = psutil.cpu_count(), psutil.cpu_count(logical=False)
    cpu_percentage = getattr(psutil, "cpu_percent", None)
    if cpu_percentage is not None:
        percentage = psutil.cpu_percent(interval=0.5)
    print(f"""{fetch}
Server Area: {zone}

{disktotal} DISK
{progress_bar_string(str(percentage_disk))} | {percentage_disk}%
Available : {diskfree}
Used      : {diskused}

{core} Core CPU
{progress_bar_string(str(percentage))} | {percentage}%
Logical   : {logic}
Frequency : {cpufrq}

{mtotal} RAM
{progress_bar_string(str(percentage_memory))} | {percentage_memory}%
Available : {mfree}
Used      : {mused}
Python3   : {pyU}
{isswap}
BANDWIDTH TOTAL
Download  : {recv}
Upload    : {sent}
""")


sys()
import platform
import socket
import psutil
import subprocess
import getpass

username = getpass.getuser()
hostname = socket.gethostname()

info = platform.freedesktop_os_release()
kernel_version = platform.release()
architecture = platform.machine()
mem = psutil.virtual_memory()
disk = psutil.disk_usage("/")
logical_cores = psutil.cpu_count(logical=True)
physical_cores = psutil.cpu_count(logical=False)
cpu_usage = psutil.cpu_percent(interval=1)
GB = 1024**3 # converts bytes into gb


def show_os():
    print(f"{'OS: '}{info['PRETTY_NAME']}", architecture)

def show_kernel_version():
    print(f"{'Kernel version: '}{kernel_version}")

def show_hostname():
    print(f"{'Hostname: '}{hostname}")

def show_username():
    print(f"{'Username: '}{username}")

def show_logical_cores():
    print(f"{'Threads: ':}{logical_cores}")

def show_physical_cores():
    print(f"{'Cores: ':}{physical_cores}")

def show_cpu_usage():
    print(f"{'CPU Usage: '}{cpu_usage}%")

def show_total_ram():
    print(f"{'Total RAM: '}{round(mem.total / GB, 2)} GB")

def show_used_ram():
    print(f"{'Used RAM: '}{round(mem.used / GB, 2)} GB")

def show_disk_total():
    print(f"{'Disk Total: '}{round(disk.total / GB, 2)} GB")

def show_disk_free():
    print(f"{'Disk Free: '}{round(disk.free / GB, 2)} GB")

def get_cpu_name():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.split(":")[1].strip()
        return "CPU not found"

def show_cpu():
    print(f"{'CPU: '}{get_cpu_name()}")

def get_gpu_name():
    try:
        result = subprocess.check_output(["lspci"], text=True)
        for line in result.splitlines():
            if "VGA" in line or "3D controller" in line:
                return line.split(":", 1)[1].strip()
    except FileNotFoundError:
        return "Error: lspci not found"
    return "GPU not found"

def show_gpu():
    print(f"{'GPU: '}{get_gpu_name()}")

def show_specs():
    print('Specs:')
    print('---------')
    show_os()
    show_kernel_version()
    show_hostname()
    show_username()
    show_cpu()
    show_physical_cores()
    show_logical_cores()
    show_cpu_usage()
    show_gpu()
    show_total_ram()
    show_used_ram()
    show_disk_total()
    show_disk_free()

def main():
    show_specs()

main()
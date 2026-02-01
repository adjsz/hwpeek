import platform
import socket
import psutil
import subprocess

mem = psutil.virtual_memory()
disk = psutil.disk_usage("/")
GB = 1024**3 # converts bytes into gb

def show_os():
    info = platform.freedesktop_os_release()
    print("OS:", info["PRETTY_NAME"])

def show_hostname():
    print("Hostname:", socket.gethostname())

def show_logical_cores():
    print("Threads:", psutil.cpu_count(logical=True))

def show_physical_cores():
    print("Cores:", psutil.cpu_count(logical=False))

def show_cpu_usage():
    print("CPU usage:", psutil.cpu_percent(interval=1), "%")

def show_total_ram():
    print("Total RAM:", round(mem.total / GB, 2), "GB") # converts bytes (B) to gigabytes (GB)

def show_used_ram():
    print("Used RAM:", round(mem.used / GB, 2), "GB") # converts bytes (B) to gigabytes (GB)

def show_disk_total():
    print("Disk total:", round(disk.total / GB, 2), "GB") # converts bytes (B) to gigabytes (GB)

def show_disk_free():
    print("Disk free:", round(disk.free / GB, 2), "GB") # converts bytes (B) to gigabytes (GB)

def get_cpu_name():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.split(":")[1].strip()
        return "CPU not found"

def show_cpu():
    print("CPU:", get_cpu_name())

def get_gpu_name():
    result = subprocess.check_output(["lspci"], text=True)
    for line in result.splitlines():
        if "VGA" in line or "3D controller" in line:
            return line.split(":", 1)[1].strip()
    return "GPU not found"
        
def show_gpu():
    print("GPU:", get_gpu_name())


def show_specs():
    print('Specs:')
    print('---------')
    show_os()
    show_hostname()
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
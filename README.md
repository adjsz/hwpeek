# hwpeek

hwpeek is a simple Linux CLI tool that displays basic system hardware and OS information.

## Installation

### Install locally

```bash
git clone https://github.com/adjsz/hwpeek.git
cd hwpeek
python3 hwpeek
```

### Install via APT

Add the repository:

```bash
echo "deb [trusted=yes] https://adjsz.github.io/hwpeek ./" | sudo tee /etc/apt/sources.list.d/hwpeek.list
sudo apt update
sudo apt install hwpeek
```

### Note:

This tool is only compatible with Linux because it relies on the command `lspci` for the GPU name as well as the Linux-specific virtual file `/proc/cpuinfo` to detect the CPU.
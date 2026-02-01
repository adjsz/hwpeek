# hwpeek

hwpeek is a simple Linux CLI tool that displays basic system hardware and OS information.

## Requirements

- Linux  
- Python 3.10+  
- `psutil`  
- `lscpu` (from `util-linux`)
- `lspci` (from `pciutils`)  

## Dependencies

```bash
pip install psutil
sudo apt install pciutils
sudo apt install util-linux
```
### If pip fails:

```bash
sudo apt install python3-psutil
```
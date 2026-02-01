# hwpeek

hwpeek is a simple Linux CLI tool that displays basic system hardware and OS information.

## Requirements

- Linux  
- Python 3.10+  
- `psutil`  
- `lspci` (from `pciutils`)  

## Dependencies

```bash
pip install psutil
sudo apt install pciutils
```
### If pip fails:

```bash
sudo apt install python3-psutil
sudo apt install pciutils
```
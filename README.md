# hwpeek

hwpeek is a simple Linux CLI tool that displays basic system hardware and OS information.

## Installation

# Install via APT

Add the repository:

```bash
echo "deb [trusted=yes] https://adjsz.github.io/REPO ./" | sudo tee /etc/apt/sources.list.d/hwpeek.list
sudo apt update
sudo apt install hwpeek

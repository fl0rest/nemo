
# Nemo

A tool for parsing Apache logs easily

## Roadmap


- Adding a TUI on top of existing functionality
## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Installation

Download nemo 

```bash
    wget https://github.com/fl0rest/nemo/archive/refs/tags/v0.1.zip
    unzip v0.1.zip
```
Or if you are running below python 3.10:

```bash
    wget https://github.com/fl0rest/nemo/archive/refs/tags/v0.1b.zip
    unzip v0.1b.zip
```

Add this to your .bashrc

```bash
    alias nemo='<path>/<to>/<nemo.py>
```
## Usage/Examples

- Find all of the IPs and limit the number of results to 10
```bash
    nemo ip -l 10
```
- Find IPs and User Agents associated with them
```bash
    nemo ip ua
```
- Search for a string and find all IPs
```bash
    nemo ip -s Chrome/98
```
- Specify a file to look through for IPs
```bash
    nemo ip -f access.log1
```

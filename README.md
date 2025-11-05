# Hackify

**This project is meant FOR EDUCATIONAL PURPOSES ONLY. I am not liable for any malicious misuse of any of the programs in this repository.**

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

# Installation

 Just download the repository and use the python scripts [Usage](#usage)

# Usage

### Basic Example
### Python Keylogger :
```python
python keylogger.py start
```
### Python Ctrl + Alt + Delete (WinLogon Screen) Detector:
```python
from hackify import WLDetector as WLD
wld=WLD()
detector=wld.detect()
# If variable detector returns True, it means user is on the win logon screen, and vice versa
```

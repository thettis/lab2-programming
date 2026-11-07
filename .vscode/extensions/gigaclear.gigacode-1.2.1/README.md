# Gigacode

Extension for frequent commands across projects

## Features

- Encryption/Decryption - Right click a .yaml file to encrypt/decrypt it

![](https://github.com/2373655r/gigacode_gif/blob/main/encrypt.gif?raw=true)

## Extension Settings

For encryption/decryption you will need the sops command to work in a regular terminal first.

Suggested setup using windows (with git bash):  
- custom terminal path = `C:\Git\bin\bash.exe`  
- custom file path separator = `/`

## Known Issues

- When using windows output files are UTF-16 encoded, UTF-8 can be achieved
by using git bash or WSL

## Release Notes

### 1.1.4

- Add support for more varied file names. Files should follow *.yaml or *.decrypted.yaml

### 1.1.3

- Bug fixes

### 1.1.2

- Added `Gigacode: Update config` to the Command Palette (ctrl+shift+p) which allows
setting a terminal path override and a file path separator override.


### 1.1.1

- Add support for wsl

### 1.0.0

- Initial release
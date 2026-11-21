JennyMod Installer For PC — Windows build notes
================================================

1. Install Python 3.11+ and pip.
2. pip install -r requirements.txt
3. pyinstaller installer/jennymod-setup.spec
4. Output: dist/JennyModSetup.exe

The exe requires Minecraft Java Edition installed and a Fabric-compatible
launcher. Run with --minecraft-dir if Game Pass / custom paths are used.
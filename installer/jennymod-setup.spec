# PyInstaller spec — builds JennyModSetup.exe for Windows.
# Build: pyinstaller installer/jennymod-setup.spec

block_cipher = None

a = Analysis(
    ['../src/jennymod_setup/__main__.py'],
    pathex=['../src'],
    binaries=[],
    datas=[('../src/jennymod_setup/data', 'jennymod_setup/data')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['tkinter', 'test'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='JennyModSetup',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None,
)
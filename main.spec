# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:/Python files/PyBattles/1v1 with mandow/Part1/main.py'],
             pathex=['E:\\Python files\\PyBattles\\1v1 with mandow\\Part1'],
             binaries=[],
             datas=[('E:/Python files/PyBattles/1v1 with mandow/Part1/bg.jpg', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/bg2.jpg', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/evil.png', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/jump.mp3', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/music.mp3', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/player.png', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/tab.wav', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/tap.mp3', '.'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/venv/Lib/site-packages/ursina', 'ursina/'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/venv/Lib/site-packages/ursina-3.6.0.dist-info', 'ursina-3.6.0.dist-info/'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/venv/Lib/site-packages/panda3d', 'panda3d/'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/venv/Lib/site-packages/panda3d-1.10.9.dist-info', 'panda3d-1.10.9.dist-info/'), ('E:/Python files/PyBattles/1v1 with mandow/Part1/venv/Lib/site-packages/panda3d_tools', 'panda3d_tools/')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='E:\\Python files\\PyBattles\\1v1 with mandow\\Part1\\vr-gaming.ico')

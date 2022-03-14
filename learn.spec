# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/Programmation/bacfr/learner/learn.py'],
             pathex=[],
             binaries=[],
             datas=[('D:/Programmation/bacfr/learner/1', '1/'), ('D:/Programmation/bacfr/learner/2', '2/'), ('D:/Programmation/bacfr/learner/3', '3/'), ('D:/Programmation/bacfr/learner/4', '4/'), ('D:/Programmation/bacfr/learner/5', '5/'), ('D:/Programmation/bacfr/learner/7', '7/'), ('D:/Programmation/bacfr/learner/8', '8/')],
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
          name='learn',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\Users\\Dan\\Downloads\\téléchargement.ico')

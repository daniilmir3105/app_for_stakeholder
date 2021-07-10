# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/Daniil/Documents/Daniil/programming/python_projects/app_for_stakeholder/main.py'],
             pathex=['C:\\Users\\Daniil\\Documents\\Daniil\\programming\\python_projects\\app_for_stakeholder'],
             binaries=[],
             datas=[('C:/Users/Daniil/Documents/Daniil/programming/python_projects/app_for_stakeholder/good_relation.png', '.'), 
            ('C:/Users/Daniil/Documents/Daniil/programming/python_projects/app_for_stakeholder/low_priority.png', '.'), 
            ('C:/Users/Daniil/Documents/Daniil/programming/python_projects/app_for_stakeholder/monitor.png', '.'), 
            ('C:/Users/Daniil/Documents/Daniil/programming/python_projects/app_for_stakeholder/not.png', '.'), 
            ('C:/Users/Daniil/Documents/Daniil/programming/python_projects/app_for_stakeholder/protect.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['interface_2', 'base_class_analys', 'become_result'],
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
          icon='C:\\Users\\Daniil\\Documents\\Daniil\\programming\\python_projects\\app_for_stakeholder\\i.ico')

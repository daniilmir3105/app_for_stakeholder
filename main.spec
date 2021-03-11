# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[r'C:\\Users\\lenovo\\Документы\\Daniil\\programming\\python\\projects\\app_for_stakeholder'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('good_relation.png', r'C:\Users\lenovo\Документы\Daniil\programming\python\projects\app_for_stakeholder', "DATA"),
            ('low_priority.png', r'C:\Users\lenovo\Документы\Daniil\programming\python\projects\app_for_stakeholder', "DATA"),
            ('monitor.png', r'C:\Users\lenovo\Документы\Daniil\programming\python\projects\app_for_stakeholder', "DATA"),
            ('not.png', r'C:\Users\lenovo\Документы\Daniil\programming\python\projects\app_for_stakeholder', "DATA"),
            ('protect.png', r'C:\Users\lenovo\Документы\Daniil\programming\python\projects\app_for_stakeholder', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Stakeholder_app.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon=r'C:\Users\lenovo\Документы\Daniil\programming\python\projects\app_for_stakeholder\Stakeholders.ico')

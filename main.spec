# -*- mode: python -*-

a = Analysis(['main.py'],
         pathex=['C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder'],
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('not.png', 'C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder\not.png', 'Data'),
            ('good_relation.png', 'C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder\good_relation.png', 'Data'),
            ('low_priority.png, 'C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder\low_priority.png', 'Data'), 
            ('monitor.png', 'C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder\monitor.png', 'Data'),
            ('protect.png', 'C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder\protect.png', 'Data')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='main.exe',
      debug=False,
      strip=None,
      upx=True,
      console=True, icon='C:\Users\Daniil\Documents\Daniil\python\projects\app_for_stakeholder\Stakeholders.ico')
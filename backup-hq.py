import os


os.system(r'start xcopy C:\"Program Files"\MongoDB\Server\4.2 C:\data\db /d/y')
os.system(r"start /min python backup.py")
os.system(r"start /min python backup_main.py")


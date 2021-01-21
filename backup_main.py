import os
import sys
import time
import filecmp
import subprocess
import ubEnigma as ub


dirs = (
        (r"C:\Users\mount\source\repos", r"M:\_BACKUP\REPOS"),
        (r"D:\mount\Downloads", r"M:\_BACKUP\DOWNLOADS"),
        (r"D:\mount\Documents", r"M:\_BACKUP\DOCUMENTS"),
        (r"D:\Internet-Marketing", r"M:\_BACKUP\IM"),
        (r"D:\_HOLOSYNC", r"M:\_BACKUP\HOLOSYNC"),
        (r"D:\mount\Music", r"M:\_BACKUP\MUSIC"),
        (r"D:\_BIZ", r"M:\_BACKUP\BIZ"),
        (r"D:\_PWA", r"M:\_BACKUP\PWA"),
        (r"C:\data\db", r"M:\_BACKUP\DB"),
        (r"C:\ProgramData\MongoDB", r"M:\_BACKUP\MONGODB "),
    )


def ensure_directory( dst ):
    '''

    If the destination folder doesn't exist, create it

    '''

    directory = os.path.dirname( dst )
    if not os.path.exists( directory ):
        os.makedirs( directory )



def compare_directories( src, dst ):
    '''

    Compares the source and destination directories.
    Returns False if not the same.
    True means both directories and files match and no backup is required.

    '''

    try:
        comp = filecmp.dircmp( src, dst )
        common = sorted( comp.common )
    except:
        return False

    left = sorted( comp.left_list )
    right = sorted( comp.right_list )
    if left != common or right != common:
        return False

    if len( comp.diff_files ):
        return False

    for subdir in comp.common_dirs:
        left_subdir = os.path.join( src, subdir )
        right_subdir = os.path.join( dst, subdir )
        return compare_directories( left_subdir, right_subdir )

    return True



def log_directory():
    '''

    Creates a LOG directory, if it does not exist
    then creates a sub-directory named for date and
    time for the backup log

    '''
    now = time.strftime("%Y-%m-%d___%H-%M")
    direct = os.path.dirname("C:\\Users\\mount\\source\\repos\\MyDashboard\\LOG\\")
    directory = direct + '\\' + now + '\\'
    if not os.path.exists( directory ):
        os.makedirs( directory )
    return directory


count = 0
logg = log_directory()
lenn = len(dirs)

for dir in dirs:

    #    src = source directory
    #    dst = destination directory
    #    swt = switches for robocopy:
    #        /xo    = only newer versions of file,
    #        /s     = all occupied sub-directories,
    #        /MT:nn = # of threads (maximum=128, default=8)
    #        /xx    = copy source file even when destination file does not exist
    #        /LOG+  = a log is created for every d in dirs. /LOG+ appends all logs to one file
    #        /r:n   = number of times to retry, default = 1,000,000
    #        /w:nn  = number of seconds to wait before retrying

    count += 1
    src, dst, swt  = dir[0], dir[1], f"/XX /r:2 /xo /s /w:5 /MT:128 /LOG+:{logg}_BACKUP.log"
    status = (compare_directories(src, dst))


    if status == False:

        ensure_directory( dst )
        compare_directories( src, dst )
        cmnd = f'robocopy {src} {dst} {swt}'
        copi = subprocess.Popen( cmnd, shell=False )
        code = copi.wait()

    codes = range(0, 9)

    if count == lenn and code in codes:
        ub.write_txt_file( 'oo.txt', 'this file has changed!' )

sys.exit()



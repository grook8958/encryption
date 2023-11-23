import subprocess
import platform

def copy_to_clipboard(txt):
    if platform.system() == 'Windows':
        cmd='echo '+txt.strip()+'|clip'
    elif platform.system() == 'Darwin' or 'Linux':
        cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)


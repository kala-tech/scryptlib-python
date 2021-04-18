import sys
import errno
from pathlib import Path

from . import compiler_wrapper


def compile_contract(f_scrypt, out_dir=None, compiler_bin=None):
    print('Compiling contract {}'.format(f_scrypt))

    f_scrypt = Path(f_scrypt)
    if not f_scrypt.is_file():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f_scrypt.name)
    
    if not compiler_bin:
        raise Exception('Auto finding sCrypt compiler is not yet implemented.') # TODO
        #compiler_bin = find_compiler()

    if not out_dir:
        out_dir = Path('./out')
    else:
        out_dir = Path(out_dir)

    if not out_dir.is_file() and not out_dir.is_dir():
        out_dir.mkdir(parents=True)
    elif not out_dir.is_dir():
        raise Exception('File "{}" is not a directory.'.format(str(out_dir)))

    compile_args = {
            'desc': True,
            'debug': True,
            'source_map': True,
            'out_dir': out_dir,
            'compiler_bin': compiler_bin
        }
    return compiler_wrapper.compile_f(f_scrypt, **compile_args)


def find_compiler():
    scryptc = None

    if sys.platform.startswith('linux'):
        scryptc = find_compiler_linux()
    elif sys.platform == 'darwin':
        pass
    elif sys.platform == 'win32' or sys.platform == 'cygwin':
        pass

    return scryptc
        

def find_compiler_linux():
    path_suffix = 'compiler/scryptc/linux/scryptc'
    if find_compiler_checklocal(path_suffix):
        pass


def find_compiler_darwin():
    path_suffix = 'compiler/scryptc/mac/scryptc'


def find_compiler_windows():
    path_suffix = 'compiler/scryptc/win32/scryptc.exe'


def find_compiler_checklocal(path_suffix):
    pass
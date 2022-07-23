r""" dir.py governs the file creation processes for this program."""
from contextlib import contextmanager
from os import chdir, getcwd, makedirs, path

@contextmanager
def change_dir(destination: str):
    """Sets a destination for exported files."""
    cwd = getcwd()
    try:
        dest = path.realpath(destination)
        makedirs(dest, exist_ok=True)
        chdir(dest)
        yield
    finally:
        chdir(cwd)
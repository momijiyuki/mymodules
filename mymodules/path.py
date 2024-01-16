import inspect
import os


def to_abs_path(fpath):
    dirpath = get_caller_path()
    return os.path.normpath(os.path.join(dirpath, fpath))

def get_caller_path() -> str:
    """関数呼び出しをたどり大元のディレクトリのパスを返す

    Returns
    -------
    str
        _description_
    """
    caller_frame = inspect.stack()[-1]
    caller_module = inspect.getmodule(caller_frame[0])

    caller_module_path = os.path.abspath(caller_module.__file__)
    return os.path.dirname(caller_module_path)

"""Test the github module.
"""
import subprocess as sp
from requests.exceptions import HTTPError
from xinstall.utils import run_cmd


def test_install_py_github():
    """Test the wajig command.
    """
    cmd = "xinstall install_py_github https://github.com/dclong/dsutil"
    run_cmd(cmd)


def test_github():
    """Test the wajig command.
    """
    cmd = "xinstall github -r dclong/xinstall -k whl -o xinstall.wheel"
    try:
        run_cmd(cmd)
    except HTTPError as err:
        if "rate limit exceeded for url" in str(err):
            return
        raise err

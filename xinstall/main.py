"""The command-line interface for xinstall.
"""
from argparse import ArgumentParser
from .utils import add_subparser
from .ai import (
    _add_subparser_kaggle,
    _add_subparser_lightgbm,
    _add_subparser_pytorch,
    _add_subparser_autogluon,
    _add_subparser_tensorflow,
    _add_subparser_pytext,
    _add_subparser_gensim,
    _add_subparser_opencv_python,
)
from .shell import (
    _add_subparser_coreutils,
    _add_subparser_shell_utils,
    _add_subparser_bash_it,
    _add_subparser_xonsh,
    _add_subparser_hyper,
    _add_subparser_openinterminal,
    _add_subparser_bash_complete,
    _add_subparser_exa,
    _add_subparser_change_shell,
    _add_subparser_wajig,
    _add_subparser_osquery,
    _add_subparser_homebrew,
)
from .ide import (
    _add_subparser_vim,
    _add_subparser_neovim,
    _add_subparser_spacevim,
    _add_subparser_ideavim,
    _add_subparser_bash_lsp,
    _add_subparser_visual_studio_code,
    _add_subparser_intellij_idea_scala,
)
from .github import (
    _add_subparser_install_py_github,
    _add_subparser_xinstall,
    _add_subparser_dsutil,
)
from .dev import (
    _add_subparser_git, _add_subparser_git_ignore, _add_subparser_poetry,
    _add_subparser_rust, _add_subparser_nodejs, _add_subparser_python3,
    _add_subparser_pyjnius, _add_subparser_ipython, _add_subparser_yapf,
    _add_subparser_openjdk, _add_subparser_sdkman, _add_subparser_cargo,
    _add_subparser_antlr, _add_subparser_pyspark, _add_subparser_spark
)
from .jupyter import (
    _add_subparser_almond,
    _add_subparser_beakerx,
    _add_subparser_jupyterlab_lsp,
    _add_subparser_itypescript,
    _add_subparser_nbdime,
    _add_subparser_evcxr_jupyter,
)
from .github import (
    _add_subparser_xinstall,
    _add_subparser_dsutil,
)
from .virtualization import (
    _add_subparser_docker,
    _add_subparser_kubernetes,
    _add_subparser_minikube,
    _add_subparser_virtualbox,
)
from .web import (
    _add_subparser_blogging,
    _add_subparser_download_tools,
    _add_subparser_dryscrape,
    _add_subparser_proxychains,
    _add_subparser_ssh_client,
    _add_subparser_ssh_server,
)
from .misc import _add_subparser_nomachine
__version__ = "0.4.7"


def version(**kwargs):
    """Print the version of xinstall.
    """
    print(__version__)


def _add_subparser_version(subparsers):
    subparser = subparsers.add_parser(
        "version",
        aliases=["ver", "v"],
        help="Print version of the xinstall package."
    )
    subparser.set_defaults(func=version)
    return subparser


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the install/configuration util.
    """
    parser = ArgumentParser(
        description="Easy installation and configuration for Unix/Linux"
    )
    parser.add_argument(
        "-s",
        "--sudo",
        dest="sudo",
        action="store_true",
        help="Run commands using sudo."
    )
    parser.add_argument(
        "-y",
        "--yes",
        dest="yes",
        action="store_true",
        help="Automatical yes (default no) to prompt questions."
    )
    subparsers = parser.add_subparsers(dest="sub_cmd", help="Sub commands.")
    # ------------------------ command-line tools ----------------------------
    _add_subparser_coreutils(subparsers)
    _add_subparser_change_shell(subparsers)
    _add_subparser_shell_utils(subparsers)
    _add_subparser_bash_it(subparsers)
    _add_subparser_xonsh(subparsers)
    _add_subparser_homebrew(subparsers)
    _add_subparser_hyper(subparsers)
    _add_subparser_openinterminal(subparsers)
    _add_subparser_bash_complete(subparsers)
    _add_subparser_wajig(subparsers)
    _add_subparser_exa(subparsers)
    _add_subparser_osquery(subparsers)
    # ------------------------ IDEs ----------------------
    _add_subparser_vim(subparsers)
    _add_subparser_neovim(subparsers)
    _add_subparser_spacevim(subparsers)
    _add_subparser_ideavim(subparsers)
    _add_subparser_visual_studio_code(subparsers)
    _add_subparser_intellij_idea_scala(subparsers)
    _add_subparser_bash_lsp(subparsers)
    # ------------------------- development related  ------------------------------
    _add_subparser_git(subparsers)
    _add_subparser_git_ignore(subparsers)
    _add_subparser_nodejs(subparsers)
    _add_subparser_evcxr_jupyter(subparsers)
    _add_subparser_python3(subparsers)
    _add_subparser_rust(subparsers)
    _add_subparser_pyjnius(subparsers)
    _add_subparser_ipython(subparsers)
    _add_subparser_yapf(subparsers)
    _add_subparser_openjdk(subparsers)
    _add_subparser_sdkman(subparsers)
    _add_subparser_poetry(subparsers)
    _add_subparser_cargo(subparsers)
    _add_subparser_antlr(subparsers)
    _add_subparser_pyspark(subparsers)
    _add_subparser_spark(subparsers)
    # ------------------------- virtualization related  ------------------------------
    _add_subparser_docker(subparsers)
    _add_subparser_kubernetes(subparsers)
    _add_subparser_minikube(subparsers)
    _add_subparser_virtualbox(subparsers)
    # ------------------------- GitHub related  ------------------------------
    _add_subparser_dsutil(subparsers)
    _add_subparser_xinstall(subparsers)
    _add_subparser_install_py_github(subparsers)
    # ------------------------- AI related  ------------------------------
    _add_subparser_kaggle(subparsers)
    _add_subparser_lightgbm(subparsers)
    _add_subparser_pytorch(subparsers)
    _add_subparser_autogluon(subparsers)
    _add_subparser_pytext(subparsers)
    _add_subparser_tensorflow(subparsers)
    _add_subparser_gensim(subparsers)
    _add_subparser_opencv_python(subparsers)
    # ------------------------- web related ------------------------------
    _add_subparser_ssh_server(subparsers)
    _add_subparser_ssh_client(subparsers)
    _add_subparser_blogging(subparsers)
    _add_subparser_proxychains(subparsers)
    _add_subparser_dryscrape(subparsers)
    _add_subparser_download_tools(subparsers)
    # ------------------------- JupyterLab related ------------------------------
    _add_subparser_beakerx(subparsers)
    _add_subparser_jupyterlab_lsp(subparsers)
    _add_subparser_itypescript(subparsers)
    _add_subparser_nbdime(subparsers)
    _add_subparser_almond(subparsers)
    # ------------------------- misc applications ------------------------------
    _add_subparser_nomachine(subparsers)
    _add_subparser_version(subparsers)
    # --------------------------------------------------------
    return parser.parse_args(args=args, namespace=namespace)


def main():
    """Run xinstall command-line interface.
    """
    args = parse_args()
    args.func(**vars(args))


if __name__ == "__main__":
    main()

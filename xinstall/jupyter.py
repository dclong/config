"""Install and configure Jupyter/Lab related tools.
"""
import logging
from .utils import (
    USER,
    HOME,
    BIN_DIR,
    GROUP,
    run_cmd,
    namespace,
    add_subparser,
    option_pip,
    option_jupyter,
)
logging.basicConfig(
    format=
    "%(asctime)s | %(module)s.%(funcName)s: %(lineno)s | %(levelname)s: %(message)s",
    level=logging.INFO
)


def nbdime(**kwargs) -> None:
    """Install and configure nbdime for comparing difference of notebooks.
    """
    args = namespace(kwargs)
    if args.install:
        run_cmd(f"{args.pip} install --user nbdime")
    if args.uninstall:
        run_cmd(f"{args.pip} uninstall nbdime")
    if args.config:
        run_cmd("nbdime config-git --enable --global")


def _add_subparser_nbdime(subparsers) -> None:
    add_subparser(subparsers, "nbdime", func=nbdime, aliases=["nbd"])


def itypescript(**kwargs) -> None:
    """Install and configure the ITypeScript kernel.
    """
    args = namespace(kwargs)
    if args.install:
        run_cmd(f"{args.prefix} npm install -g --unsafe-perm itypescript")
        run_cmd(f"{args.prefix} its --ts-hide-undefined --install=global")
    if args.uninstall:
        run_cmd(f"{args.prefix} jupyter kernelspec uninstall typescript")
        run_cmd(f"{args.prefix} npm uninstall itypescript")
    if args.config:
        pass


def _add_subparser_itypescript(subparsers) -> None:
    add_subparser(subparsers, "iTypeScript", func=itypescript, aliases=["its"])


def jupyterlab_lsp(**kwargs) -> None:
    """Install jupyterlab-lsp.
    """
    args = namespace(kwargs)
    if args.install:
        cmd = f"""{args.pip} install jupyter-lsp \
                && {args.prefix} {args.jupyter} labextension install @krassowski/jupyterlab-lsp \
                && {args.pip} install python-language-server[all] pyls-mypy"""
        run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        pass


def _jupyterlab_lsp_args(subparser) -> None:
    option_pip(subparser)
    option_jupyter(subparser)


def _add_subparser_jupyterlab_lsp(subparsers) -> None:
    add_subparser(
        subparsers,
        "jupyterlab-lsp",
        func=jupyterlab_lsp,
        aliases=["jlab-lsp", "jlab_lsp"],
        add_argument=_jupyterlab_lsp_args,
    )


def beakerx(**kwargs) -> None:
    """Install/uninstall/configure the BeakerX kernels.
    """
    args = namespace(kwargs)
    if args.install:
        run_cmd(f"{args.pip} install --user beakerx")
        run_cmd(f"{args.prefix} beakerx install")
        run_cmd(
            f"{args.prefix} jupyter labextension install @jupyter-widgets/jupyterlab-manager",
        )
        run_cmd(f"{args.prefix} jupyter labextension install beakerx-jupyterlab")
    if args.uninstall:
        run_cmd(f"{args.prefix} jupyter labextension uninstall beakerx-jupyterlab")
        run_cmd(
            f"{args.prefix} jupyter labextension uninstall @jupyter-widgets/jupyterlab-manager"
        )
        run_cmd(f"{args.prefix} beakerx uninstall")
        run_cmd(f"{args.pip} uninstall beakerx")
    if args.config:
        run_cmd(f"{args.prefix} chown -R {USER}:{GROUP} {HOME}")


def _add_subparser_beakerx(subparsers) -> None:
    add_subparser(subparsers, "BeakerX", func=beakerx, aliases=["bkx", "bk"])


def almond(**kwargs) -> None:
    """Install/uninstall/configure the Almond Scala kernel.
    """
    args = namespace(kwargs)
    if args.almond_version:
        args.install = True
        if not args.almond_version.startswith(":"):
            args.almond_version = ":" + args.almond_version
    if args.scala_version:
        args.install = True
        args.scala_version = f"--scala {args.scala_version}"
    if args.install:
        coursier = BIN_DIR / "coursier"
        run_cmd(
            f"curl -L -o {coursier} https://git.io/coursier-cli && chmod +x {coursier}"
        )
        run_cmd(
            f"{args.prefix} /usr/local/bin/coursier launch almond{args.almond_version} {args.scala_version} --quiet -- --install --global"
        )
    if args.config:
        pass


def _almond_args(subparser) -> None:
    subparser.add_argument(
        "-a",
        "--almond-version",
        dest="almond_version",
        default="",
        help="The version (the latest supported by default) of Almond to install."
    )
    subparser.add_argument(
        "-s",
        "--scala-version",
        dest="scala_version",
        default="",
        help="The version (the latest supported by default) of Scala to install."
    )


def _add_subparser_almond(subparsers) -> None:
    add_subparser(
        subparsers,
        "Almond",
        func=almond,
        aliases=["al", "amd"],
        add_argument=_almond_args
    )


def evcxr_jupyter(**kwargs) -> None:
    """Install the evcxr Rust kernel for Jupyter/Lab server.
    """
    args = namespace(kwargs)
    if args.install:
        cmd = f"""{args.prefix} apt-get install {args.yes_s} cmake cargo \
            && cargo install --force evcxr_jupyter \
            && {HOME}/.cargo/bin/evcxr_jupyter --install"""
        run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        cmd = f"""{HOME}/.cargo/bin/evcxr_jupyter --uninstall \
            && cargo uninstall evcxr_jupyter
            """
        run_cmd(cmd)


def _add_subparser_evcxr_jupyter(subparsers) -> None:
    add_subparser(subparsers, "evcxr_jupyter", func=evcxr_jupyter, aliases=["evcxr"])

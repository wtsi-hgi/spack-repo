from spack.package import *


class PyMber(PythonPackage):
    """mBER: Manifold Binder Engineering and Refinement.

    Core Python library for modular protein binder design workflows.
    See the "protocols" subpackage upstream for optional CLI tools.
    """

    homepage = "https://github.com/manifoldbio/mber-open"
    git = "https://github.com/manifoldbio/mber-open.git"

    license("MIT")

    # No official releases yet; use latest commit with date-based version.
    version("20251029", commit="fb3e6ae00b6d1e71a326ad4651dbc5f635dbf5f0")

    # Python build/run requirements
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    # Minimal runtime deps to support import and common utilities; heavier ML
    # stacks are intentionally omitted as optional dependencies are handled
    # by users or protocol packages.
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))

    def patch(self):
        # Upstream uses implicit namespace packages (no __init__.py under src/mber)
        # but setup.py calls find_packages, which omits these. Switch to
        # find_namespace_packages so package modules are included.
        filter_file(
            r"from setuptools import setup, find_packages",
            "from setuptools import setup, find_namespace_packages",
            "setup.py",
            string=True,
        )
        # Replace find_packages(...) with find_namespace_packages(...) everywhere
        filter_file(r"find_packages\((.*?)\)", r"find_namespace_packages(\1)", "setup.py")

    @run_after("install")
    def install_test(self):
        # Basic import test; core package should import without optional ML deps
        python("-c", "import mber")

        # Add test to check mber-vhh binary exists and runs
        mber_vhh = join_path(self.prefix.bin, "mber-vhh")
        bash = which("bash")
        bash(mber_vhh, "--help")

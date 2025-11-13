from spack.package import *


class PyMber(PythonPackage):
    """Manifold Binder Engineering and Refinement (mBER):
    an open-source protein design framework for antibody binder design.
    """

    homepage = "https://github.com/manifoldbio/mber-open"
    git = "https://github.com/manifoldbio/mber-open.git"

    license("MIT")

    # No tagged releases; track latest known commit by date.
    # Version is YYYYMMDD of the commit date per repo guidelines.
    version(
        "20251029",
        commit="fb3e6ae00b6d1e71a326ad4651dbc5f635dbf5f0",
        submodules=False,
    )

    # Build system
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    # Minimal runtime needed for a lightweight import test.
    # The utilities module references Biopython's Bio.PDB types.
    depends_on("py-biopython", type=("build", "run"))

    def patch(self):
        # The upstream setup.py may include multiple concatenated blocks and
        # references to a requirements.txt with heavy GPU deps. Replace it with
        # a minimal, deterministic setup.py so Spack controls dependencies.
        sanitized = (
            "from setuptools import setup, find_namespace_packages\n"
            "setup(\n"
            "    name=\"mber\",\n"
            "    version=\"1.0.0\",\n"
            "    packages=find_namespace_packages(where=\"src\"),\n"
            "    package_dir={\"\": \"src\"},\n"
            "    python_requires=\">=3.11\",\n"
            "    install_requires=[],\n"
            ")\n"
        )
        with open("setup.py", "w", encoding="utf-8") as f:
            f.write(sanitized)

    @run_after("install")
    def install_test(self):
        # mber does not expose a CLI in the core package. Perform a lightweight
        # import test on a submodule that doesn't pull heavy ML deps.
        with working_dir("spack-test", create=True):
            python("-c", "import mber.utils; print(mber.utils.__all__)\n")

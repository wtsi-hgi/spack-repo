import os
from spack.package import *
from spack.util.executable import Executable


class PyMber(PythonPackage):
    """
    Manifold Binder Engineering and Refinement (MBER):
    A package for format-specific protein binder design.

    Upstream repository contains additional setup steps that we replicate:
    - Install editable protocols package from ./protocols
    - Download AlphaFold2 weights via download_af_weights.sh
    """

    homepage = "https://github.com/manifoldbio/mber-open"
    git      = "https://github.com/manifoldbio/mber-open.git"

    maintainers("softpack-bot")

    # No releases/tags; pin to latest commit with date-based version per guidelines
    version("20251029", commit="fb3e6ae00b6d1e71a326ad4651dbc5f635dbf5f0")

    # Python build metadata
    # Upstream requires Python >= 3.11
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type=("build", "run"))
    depends_on("wget", type="run")

    # Many heavy ML/runtime requirements are pulled via pip as upstream expects.
    # We intentionally avoid declaring them as Spack deps to prevent widespread
    # concretization conflicts and to honor upstream wheels (CUDA/JAX/PyTorch).

    # Project follows src-layout
    build_directory = "."

    def patch(self):
        # Ensure setuptools uses namespace package discovery for src-layout.
        # Upstream may mix find_namespace_packages import with find_packages usage.
        # Ensure the import brings in find_namespace_packages
        filter_file(
            "from setuptools import setup, find_packages",
            "from setuptools import setup, find_namespace_packages",
            "setup.py",
            string=True,
        )
        filter_file(
            "packages=find_packages(",
            "packages=find_namespace_packages(",
            "setup.py",
            string=True,
        )
        # Remove/skip conda-only dependencies that aren't available on PyPI
        # (pdbfixer is provided via conda/openmm in upstream environment.yml)
        filter_file(r"^pdbfixer\s*$", "", "requirements.txt")

    def install(self, spec, prefix):
        # Ensure upstream runtime requirements are satisfied using pip.
        python = Executable(self.spec["python"].command.path)

        # Install Python requirements.txt first to satisfy install_requires
        with working_dir(self.build_directory):
            python("-m", "pip", "install", "--upgrade", "pip")
            python(
                "-m",
                "pip",
                "install",
                "-r",
                "requirements.txt",
            )

        # Perform the standard PythonPackage install for mber itself
        super().install(spec, prefix)

        # Install mber-protocols (editable) from the repository's protocols directory
        with working_dir(self.stage.source_path):
            python(
                "-m",
                "pip",
                "install",
                "-e",
                "protocols",
            )

        # Download AlphaFold2 weights using the provided script
        # This installs to $HOME/.mber/af_params as per upstream script.
        bash = which("bash")
        with working_dir(self.stage.source_path):
            env = os.environ.copy()
            # Ensure wget from Spack is on PATH for the script
            if "wget" in self.spec:
                env["PATH"] = join_path(self.spec["wget"].prefix.bin, ".") + os.pathsep + env.get("PATH", "")
            bash("download_af_weights.sh", env=env)

    @run_after("install")
    def install_test(self):
        # Basic import test; no CLI exposed upstream. If a CLI appears later,
        # extend this to exercise it (e.g., `mber --help`).
        with working_dir("spack-test", create=True):
            python = Executable(self.spec["python"].command.path)
            pyver = str(self.spec["python"].version.up_to(2))
            site_pkgs_lib = join_path(self.prefix, "lib", f"python{pyver}", "site-packages")
            site_pkgs_lib64 = join_path(self.prefix, "lib64", f"python{pyver}", "site-packages")
            env = os.environ.copy()
            env["PYTHONPATH"] = os.pathsep.join([
                site_pkgs_lib,
                site_pkgs_lib64,
                env.get("PYTHONPATH", ""),
            ])
            python("-c", "import mber", env=env)

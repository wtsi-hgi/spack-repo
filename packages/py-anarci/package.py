from spack.package import *
from glob import glob
import os


class PyAnarci(Package):
    """
    ANARCI: Antibody Numbering and Receptor ClassIfication. Provides antibody
    and T-cell receptor sequence numbering and classification, relying on
    HMMER and MUSCLE during installation to build HMM databases from IMGT
    germlines.
    """

    homepage = "https://github.com/oxpig/ANARCI"
    git      = "https://github.com/oxpig/ANARCI.git"

    # No tagged releases; use latest known commit with date as version id
    version("20240521", commit="79f6c575056dedef86cb8f405ebb039197923eec")

    # Mark as a Python extension so Spack sets PYTHONPATH on load
    extends("python")

    # Use a custom install via setup.py to avoid pip/wheel issues
    # Note: Some Spack versions only support the pip backend for PythonPackage.
    # We patch setup.py to disable its custom installer so wheel builds succeed.

    # Build dependencies
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")

    # Runtime/build requirements from repo and build pipeline
    depends_on("py-biopython", type=("build", "run"))
    depends_on("hmmer@3.1:", type=("build", "run"))
    depends_on("muscle", type=("build", "run"))

    # Basic smoke test: verify installed files exist
    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Verify CLI installed and HMM database present
            assert os.path.isfile(join_path(self.prefix.bin, "ANARCI"))
            hmm_p = glob(join_path(self.prefix, "lib", "python*", "site-packages", "anarci", "dat", "HMMs", "ALL.hmm.h3p"))
            assert hmm_p and os.path.isfile(hmm_p[0])

    def install(self, spec, prefix):
        # Patch setup.py to disable the upstream CustomInstallCommand that would
        # write outside the prefix and perform network I/O during install.
        filter_file(
            r"from distutils.core import setup",
            "from setuptools import setup",
            "setup.py",
            string=True,
        )
        filter_file(r"cmdclass\s*=\s*\{[^\}]*\}", "cmdclass={}", "setup.py")

        # Install via pip into prefix (after patching setup.py)
        python = spec["python"].command
        python("-m", "pip", "install", ".", "--no-deps", "--no-build-isolation", f"--prefix={prefix}")

        # Build HMMs from IMGT data (requires hmmer + muscle)
        with working_dir("build_pipeline"):
            bash = which("bash")
            bash("RUN_pipeline.sh")

        # Locate installed site-packages and copy data into package dir
        sp_dirs = glob(join_path(prefix, "lib", "python*", "site-packages"))
        if not sp_dirs:
            raise InstallError("Could not locate site-packages under prefix")
        anarci_pkg = join_path(sp_dirs[0], "anarci")
        mkdirp(join_path(anarci_pkg, "dat"))
        install(join_path("build_pipeline", "curated_alignments", "germlines.py"), anarci_pkg)
        install_tree(join_path("build_pipeline", "HMMs"), join_path(anarci_pkg, "dat", "HMMs"))

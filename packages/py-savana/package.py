from spack.package import *


class PySavana(PythonPackage):
    """SAVANA - somatic structural variant caller for long reads."""

    homepage = "https://github.com/cortes-ciriano-lab/savana"
    git = "https://github.com/cortes-ciriano-lab/savana.git"

    license("Apache-2.0")

    # Use full commit hash for the tagged release
    version("1.3.5", commit="83c915e9ed97d5c75f391663e2d2e314685f709b")

    # Python build system
    depends_on("py-setuptools", type="build")

    # Runtime requirements from requirements.txt
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-cyvcf2", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))

    # Project targets Python 3.9 per classifiers in setup.py
    depends_on("python@3.9:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Basic import test to verify installation
            python("-c", "import savana; print('ok')")

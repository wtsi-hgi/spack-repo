import os

from spack.package import *


class PyScikitBio(PythonPackage):
    """Data structures, algorithms and educational resources for bioinformatics."""

    homepage = "https://scikit.bio"
    pypi = "scikit-bio/scikit_bio-0.7.3.tar.gz"

    license("BSD-3-Clause")

    version("0.7.3", sha256="2492ebf2f6432d24c1030a0cd96d7708c2b57bc31b097a5ec838881792401ec5")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-numpy@2.0:", type=("build", "run"))
    depends_on("py-requests@2.20:", type=("build", "run"))
    depends_on("py-decorator@3.4.2:", type=("build", "run"))
    depends_on("py-natsort@4.0.3:", type=("build", "run"))
    depends_on("py-pandas@1.5:", type=("build", "run"))
    depends_on("py-scipy@1.9:1.16", type=("build", "run"))
    depends_on("py-h5py@3.6:", type=("build", "run"))
    depends_on("py-biom-format@2.1.16:", type=("build", "run"))
    depends_on("py-statsmodels@0.14:", type=("build", "run"))
    depends_on("py-patsy@0.5:", type=("build", "run"))
    depends_on("py-array-api-compat@1.3:", type=("build", "run"))

    def patch(self):
        filter_file('from Cython.Build import cythonize', 'cythonize = None', "setup.py", string=True)
        filter_file('ext = ".pyx"', 'ext = ".c"', "setup.py", string=True)
        filter_file('extensions = cythonize(extensions, force=True)', '', "setup.py", string=True)
        filter_file('license = "BSD-3-Clause"', 'license = {text = "BSD-3-Clause"}', "pyproject.toml", string=True)
        filter_file('license-files = ["LICENSE.txt"]', '', "pyproject.toml", string=True)

    @run_after("install")
    def install_test(self):
        python = which(self.spec["python"].command.path)
        python(
            "-c",
            (
                "import os, sys; "
                "sys.path=[p for p in sys.path if p and os.path.realpath(p)!=os.path.realpath(os.getcwd())]; "
                f"sys.path.insert(0, {self.prefix.lib.python3.site_packages!r}); "
                "import skbio"
            ),
        )

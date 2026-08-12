from spack.package import *


class PyBiomFormat(PythonPackage):
    """Biological Observation Matrix (BIOM) format."""

    homepage = "http://www.biom-format.org"
    pypi = "biom-format/biom-format-2.1.16.tar.gz"

    license("BSD-3-Clause")

    version("2.1.16", sha256="47f88d57a94ecaa4d06f3578ca394e78db6d12e46ab0886634743181e67dcfc9")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-numpy@1.9.2:", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-scipy@1.3.1:", type=("build", "run"))
    depends_on("py-pandas@0.20:", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        biom = which(join_path(self.prefix.bin, "biom"))
        biom("--help")

from spack.package import *


class PyStarrpeaker(PythonPackage):
    """STARRPeaker is a peak caller for STARR-seq experiments."""

    homepage = "https://github.com/gersteinlab/starrpeaker"
    url = "https://github.com/gersteinlab/starrpeaker/archive/refs/tags/v1.2.tar.gz"

    license("GPL-3.0-or-later", "LICENSE")

    version("1.2", sha256="6ea2b136576645f9e4207df3e2b88ec157a84df356ef51be603c2cc1444ec6b4")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-statsmodels@:0.10.2", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        with working_dir("spack-test", create=True):
            python("-c", "import starrpeaker")

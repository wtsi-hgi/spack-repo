from spack.package import *


class RMultipower(RPackage):
    """Estimation of sample size in multi-omic experiments."""

    homepage = "https://github.com/ConesaLab/MultiPower"
    git = "https://github.com/ConesaLab/MultiPower.git"

    license("GPL-2")

    version("20250118", commit="be6285242bfa4f53ac197ee9792c8e3b280d22c2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-fdrsampsize", type=("build", "run"))
    depends_on("r-lpsolve", type=("build", "run"))

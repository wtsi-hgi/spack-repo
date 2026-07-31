from spack.package import *


class RCpp11armadillo(RPackage):
    """An Armadillo Interface

    Provides function declarations and inline function definitions that
    facilitate communication between R and the Armadillo C++ library for
    linear algebra and scientific computing.
    """

    homepage = "https://github.com/pachadotdev/cpp11armadillo"
    cran = "cpp11armadillo"

    license("Apache-2.0")

    version("0.5.4", md5="d4fd5fa97cf7100bdf45e1ff2e9b531a")

    depends_on("r@3.5.0:", type=("build", "run"))
    depends_on("r-cpp11", type=("build", "run"))


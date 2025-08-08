from spack.package import *


class RShinyfiles(RPackage):
    """A Shiny extension for client-side file system access."""

    cran = "shinyFiles"

    version("0.9.3", sha256="4a72e165ee8a6e8256988f27286a2cfc4d7a42e2a902f4f2a728b1c237c07286")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-shiny@0.14:", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-miniui", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-zip", type=("build", "run"))

from spack.package import *


class RShinyjs(RPackage):
    """Easily improve the user experience of your Shiny apps in seconds with
    little to no JavaScript required."""

    cran = "shinyjs"

    version("2.1.0", sha256="7ec20cbf1b1fd7a32d85a56dfc0df8b5f67c828d241da400a21d893cb37ea9c5")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-shiny@0.12:", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))

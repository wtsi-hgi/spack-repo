from spack.package import *


class RShinyjs(RPackage):
    """Easily improve the user experience of your Shiny apps in seconds with
    little to no JavaScript required."""

    cran = "shinyjs"

    version("2.1.0", sha256="4f2a00d32759f0e197d71d3aaa3decbc3f455938590d0f1f491b63af7e1459d9")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-shiny@0.12:", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))

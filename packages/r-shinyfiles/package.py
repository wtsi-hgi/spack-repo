from spack.package import *


class RShinyfiles(RPackage):
    """A Shiny extension for client-side file system access."""

    cran = "shinyFiles"

    version("0.9.3", sha256="9b8710b12f1c3d254f5ad5de6522a5c87f2e0138737b83b03587965e7fb9ce34")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-shiny@0.14:", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-miniui", type=("build", "run"))
    depends_on("r-zip", type=("build", "run"))

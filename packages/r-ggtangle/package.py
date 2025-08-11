from spack.package import *


class RGgtangle(RPackage):
    """Tanglegram utilities for 'ggplot2'/'ggtree' style plots."""

    cran = "ggtangle"

    version("0.0.7", sha256="c77c6c4c17c1ba4f60ec8ce7b4bfdcc71300fb1003010a5873ff9a3f684b7b62")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-ggfun@0.1.7:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-yulab-utils@0.1.7:", type=("build", "run"))

from spack.package import *


class RKbet(RPackage):
    """k-nearest neighbour batch effect test.

    Detects batch effects in high-dimensional data based on a chi-squared test.
    """

    homepage = "https://github.com/theislab/kBET"
    git = "https://github.com/theislab/kBET.git"

    license("Apache-2.0")

    # Latest commit as of 2024-01-26
    version("20240126", commit="afc5f431bcbefd73267acc066a0f2e4eaa10a355")

    # Core R dependency
    depends_on("r", type=("build", "run"))

    # Imports from DESCRIPTION
    with default_args(type=("build", "run")):
        # Imports
        depends_on("r-fnn")
        depends_on("r-rcolorbrewer")
        depends_on("r-ggplot2")
        depends_on("r-cluster")
        depends_on("r-mass")

        # Optional 'Suggests' are intentionally omitted for R packages

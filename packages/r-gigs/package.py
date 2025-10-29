from spack.package import *


class RGigs(RPackage):
    """Assess fetal, newborn, and child growth using international standards.

    Provides conversions between anthropometric measures and z-scores/centiles
    and classifies growth using WHO and INTERGROWTH-21st standards.
    """

    homepage = "https://github.com/ropensci/gigs"
    url = "https://github.com/ropensci/gigs/archive/refs/tags/v0.5.2.tar.gz"
    git = "https://github.com/ropensci/gigs.git"

    license("GPL-3.0-or-later")

    version("0.5.2", sha256="ffcb113d4b21d1edbe4c28d7b5abf7d19e00c7fab73603d20877e36050ffb0f6")

    depends_on("r@4.1.0:", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-gamlss-dist", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-vctrs@0.4.0:", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))


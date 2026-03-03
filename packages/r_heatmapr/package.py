from spack.package import *


class RHeatmapr(RPackage):
    """Create Heatmaps using Base Graphics.

    HeatmapR provides utilities for generating heatmaps using base R graphics.
    """

    homepage = "https://github.com/DillonHammill/HeatmapR"
    git = "https://github.com/DillonHammill/HeatmapR.git"

    maintainers("softpack-bot")

    license("GPL-2.0-only")

    # No releases/tags; track latest commit with date-based version id
    version("20230424", commit="05a6e191dcbab0ac89301de93b9f22327fa2e2bf")

    depends_on("r@3.5:", type=("build", "run"))


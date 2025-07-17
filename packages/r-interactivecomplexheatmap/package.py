# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractivecomplexheatmap(RPackage):
    """Make Interactive Complex Heatmaps

    This package can easily make heatmaps which are produced by the ComplexHeatmap package into interactive applications. It provides two types of interactivities: 1. on the interactive graphics device, and 2. on a Shiny app. It also provides functions for integrating the interactive heatmap widgets for more complex Shiny app development.
    """

    homepage = "https://github.com/jokergoo/InteractiveComplexHeatmap"
    bioc = "InteractiveComplexHeatmap"

    version("1.16.0", commit="3c271570bd71e76b211cd651c5f466ae781ad20c")
    version("1.10.0", commit="020c73a65ebbb4aa5827e03786f67a3b2fd4a6fa")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-complexheatmap@2.11:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-getoptlong", type=("build", "run"))
    depends_on("r-s4vectors@0.26.1:", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-kableextra@1.3.1:", type=("build", "run"))
    depends_on("r-svglite", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-clisymbols", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-fontawesome", type=("build", "run"))

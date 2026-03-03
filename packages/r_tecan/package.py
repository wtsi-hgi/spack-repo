# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTecan(RPackage):
    """TECAN-reader based yeast growth measurements in R"""

    homepage = "https://github.com/lehner-lab/TECAN_analysis"
    #git = "https://github.com/lehner-lab/TECAN_analysis"

    version("0.7.1", sha256="26b7cdaae464d37a93eac0af05232dda48643a23f8087034e291b0a577049475")
    #version("1.0", commit="ec58546")

    cran = "argparser"

    depends_on("r+X", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-beeswarm", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))

    depends_on("r-growthrates", type=("build", "run"))


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmanh(RPackage):
    """Visualization Tool for GWAS Result

    Manhattan plot and QQ Plot are commonly used to visualize the end result of Genome Wide Association Study. The "ggmanh" package aims to keep the generation of these plots simple while maintaining customizability. Main functions include manhattan_plot, qqunif, and thinPoints.
    """

    bioc = "ggmanh"

    version("1.12.0", commit="a314ecb9a01273b3bf8152317299b8e8efbf2537")
    version("1.6.0", commit="48558701e5fe97fcf245931f8257529bcf0d6fb2")

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gdsfmt", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-seqarray@1.32:", type=("build", "run"))

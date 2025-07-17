# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowclean(RPackage):
    """flowClean

    A quality control tool for flow cytometry data based on compositional data analysis.
    """

    bioc = "flowClean"

    version("1.46.0", commit="15ad65db0c98e4a7524a05245edc9c5599843c17")
    version("1.40.0", commit="aa2d962d0ca0d2f08a98b351761616eb53d956c6")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-bit", type=("build", "run"))
    depends_on("r-changepoint", type=("build", "run"))
    depends_on("r-sfsmisc", type=("build", "run"))

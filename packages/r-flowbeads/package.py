# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowbeads(RPackage):
    """flowBeads: Analysis of flow bead data

    This package extends flowCore to provide functionality specific to bead data. One of the goals of this package is to automate analysis of bead data for the purpose of normalisation.
    """

    bioc = "flowBeads"

    version("1.46.0", commit="6ceaa6aea927eaae257aaa9f7ae504cfe964fc4e")
    version("1.40.0", commit="9631ea04e3cd393a68343ebeb117f1910185f6d8")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-rrcov", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))

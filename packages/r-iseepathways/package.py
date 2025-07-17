# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseepathways(RPackage):
    """iSEE extension for panels related to pathway analysis

    This package contains diverse functionality to extend the usage of the iSEE package, including additional classes for the panels or modes facilitating the analysis of pathway analysis results. This package does not perform pathway analysis. Instead, it provides methods to embed precomputed pathway analysis results in a SummarizedExperiment object, in a manner that is compatible with interactive visualisation in iSEE applications.
    """

    homepage = "https://github.com/iSEE/iSEEpathways"
    bioc = "iSEEpathways"

    version("1.6.0", commit="464af3f4b5052f174843a54b5f83e4b0582a6e90")
    version("1.0.0", commit="23073a987477cd5b4e079cc1f8e08106da324d18")

    depends_on("r-isee", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))

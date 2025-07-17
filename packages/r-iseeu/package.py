# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseeu(RPackage):
    """iSEE Universe

    iSEEu (the iSEE universe) contains diverse functionality to extend the usage of the iSEE package, including additional classes for the panels, or modes allowing easy configuration of iSEE applications.
    """

    homepage = "https://github.com/iSEE/iSEEu"
    bioc = "iSEEu"

    version("1.20.0", commit="313560b16c1f599974d5c67177c1f3e6e0c46120")
    version("1.14.0", commit="61cbb7adeb0b8fd456c6af14801efef6a852d65b")

    depends_on("r-isee", type=("build", "run"))
    depends_on("r-iseehex", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-ggplot2@3.4:", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-colourpicker", type=("build", "run"))
    depends_on("r-shinyace", type=("build", "run"))

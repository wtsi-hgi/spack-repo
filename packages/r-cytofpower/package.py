# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytofpower(RPackage):
    """Power analysis for CyTOF experiments

    This package is a tool to predict the power of CyTOF experiments in the context of differential state analyses. The package provides a shiny app with two options to predict the power of an experiment: i. generation of in-sicilico CyTOF data, using users input ii. browsing in a grid of parameters for which the power was already precomputed.
    """

    bioc = "CyTOFpower"

    version("1.14.0", commit="bcdfa4bc01b9313354fa078ab030c260746935d9")
    version("1.8.0", commit="d62a254879db407ffcbd98d279e5b9be5d3ced08")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-cytoglmm", type=("build", "run"))
    depends_on("r-diffcyt", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyfeedback", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-shinymatrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))

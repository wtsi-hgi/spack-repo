# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtsge(RPackage):
    """Clustering of Time Series Gene Expression data

    Methodology for supervised clustering of potentially many predictor variables, such as genes etc., in time series datasets Provides functions that help the user assigning genes to predefined set of model profiles.
    """

    homepage = "https://github.com/michalsharabi/ctsGE"
    bioc = "ctsGE"

    version("1.34.0", commit="4a612dac8e1820624253a208f85707f2d963d6fa")
    version("1.28.0", commit="18cd56ef2dfb1ef059b33e163781d2cc407a221d")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-ccapp", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))

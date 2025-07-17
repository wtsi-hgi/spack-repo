# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowtime(RPackage):
    """Annotation and analysis of biological dynamical systems using flow cytometry

    This package facilitates analysis of both timecourse and steady state flow cytometry experiments. This package was originially developed for quantifying the function of gene regulatory networks in yeast (strain W303) expressing fluorescent reporter proteins using BD Accuri C6 and SORP cytometers. However, the functions are for the most part general and may be adapted for analysis of other organisms using other flow cytometers. Functions in this package facilitate the annotation of flow cytometry data with experimental metadata, as often required for publication and general ease-of-reuse. Functions for creating, saving and loading gate sets are also included. In the past, we have typically generated summary statistics for each flowset for each timepoint and then annotated and analyzed these summary statistics. This method loses a great deal of the power that comes from the large amounts of individual cell data generated in flow cytometry, by essentially collapsing this data into a bulk measurement after subsetting. In addition to these summary functions, this package also contains functions to facilitate annotation and analysis of steady-state or time-lapse data utilizing all of the data collected from the thousands of individual cells in each sample.
    """

    bioc = "flowTime"

    version("1.32.0", commit="2ca5ff9c36d579fb0bd2cf39c46016543f3790fa")
    version("1.26.0", commit="ae5dcddefa6174b7ede27b64891c9263ad1566c7")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-dplyr@1:", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmixer(RPackage):
    """Omixer: multivariate and reproducible sample randomization to proactively counter batch effects in omics studies

    Omixer - an Bioconductor package for multivariate and reproducible sample randomization, which ensures optimal sample distribution across batches with well-documented methods. It outputs lab-friendly sample layouts, reducing the risk of sample mixups when manually pipetting randomized samples.
    """

    bioc = "Omixer"

    version("1.18.0", commit="d7f439175fdc9237e95880374dc19216522cf57d")
    version("1.12.0", commit="4356e126018bde6923a01148da1fafd1a8e1a448")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))

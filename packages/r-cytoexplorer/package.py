# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytoexplorer(RPackage):
    """Interactive Analysis of Cytometry Data.

    CytoExploreR provides an intuitive and interactive approach to analysing
    cytometry data in R, integrating conventional and cutting-edge tools under
    a unified, open-source framework.
    """

    homepage = "https://github.com/DillonHammill/CytoExploreR"
    git = "https://github.com/DillonHammill/CytoExploreR.git"

    license("GPL-2.0-only")

    # Pin to latest commit on the 'refine' branch, named as 2.0.15
    version("2.0.15", commit="69088a6c5955afb2a2576c63e162de11ded7a882")

    depends_on("r@3.5.0:", type=("build", "run"))

    # Depends / Imports from DESCRIPTION (base packages excluded)
    with default_args(type=("build", "run")):
        depends_on("r-flowcore@2.3:")
        depends_on("r-flowworkspace@4.3.1:")
        depends_on("r-opencyto@1.25.2:")

        depends_on("r-biocgenerics")
        depends_on("r-bslib")
        depends_on("r-data-table")
        depends_on("r-dataeditr@0.1.2:")
        depends_on("r-dplyr")
        depends_on("r-future")
        depends_on("r-future-apply")
        depends_on("r-kernsmooth")
        depends_on("r-mass")
        depends_on("r-progress")
        depends_on("r-purrr")
        depends_on("r-heatmapr")
        depends_on("r-reticulate")
        depends_on("r-robustbase")
        depends_on("r-rhandsontable@0.3.8:")
        depends_on("r-shiny")
        depends_on("r-tidyr")
        depends_on("r-visnetwork")
        depends_on("r-xml")
        depends_on("r-rcpp")  # Also in LinkingTo

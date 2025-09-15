# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytoexplorer(RPackage):
    """Interactive Analysis of Cytometry Data.

    An intuitive and interactive approach to analysing cytometry data in R,
    integrating conventional and cutting-edge cytometry analysis tools under a
    unified open-source framework.
    """

    homepage = "https://github.com/DillonHammill/CytoExploreR"
    git = "https://github.com/DillonHammill/CytoExploreR.git"

    # No official releases/tags upstream; track a dated commit per guidelines
    version("20250320", commit="71a8da6fabd2843ad8f35b30b455e4fcb95a3147")

    # R version requirement from DESCRIPTION
    depends_on("r@3.5.0:", type=("build", "run"))

    # Depends (with minimal version bounds where specified)
    with default_args(type=("build", "run")):
        depends_on("r-biocgenerics")
        depends_on("r-bslib")
        depends_on("r-data-table")
        depends_on("r-dplyr")
        depends_on("r-embedsom")
        depends_on("r-flowai")
        depends_on("r-gtools")
        depends_on("r-mass")
        depends_on("r-magrittr")
        depends_on("r-purrr")
        depends_on("r-robustbase")
        depends_on("r-rtsne")
        depends_on("r-rsvd")
        depends_on("r-shiny")
        depends_on("r-tibble")
        depends_on("r-tidyr")
        depends_on("r-umap")
        depends_on("r-visnetwork")

    # Core Bioconductor dependencies
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowworkspace", type=("build", "run"))
    depends_on("r-opencyto", type=("build", "run"))
    # Other runtime dependencies
    depends_on("r-rhandsontable", type=("build", "run"))
    depends_on("r-superheat", type=("build", "run"))

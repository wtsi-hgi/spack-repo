# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytoExploreR(RPackage):
    """Interactive Analysis of Cytometry Data.

    CytoExploreR provides an intuitive and interactive approach to analysing
    cytometry data in R, integrating conventional and modern analysis tools
    within a unified open-source framework.
    """

    homepage = "https://github.com/DillonHammill/CytoExploreR"
    git = "https://github.com/DillonHammill/CytoExploreR.git"

    license("GPL-2.0-only")

    # No formal releases; track the latest known good commit.
    version("20250320", commit="71a8da6fabd2843ad8f35b30b455e4fcb95a3147")

    # R version
    depends_on("r@3.5.0:", type=("build", "run"))

    # Core dependencies (mix of CRAN and Bioconductor packages)
    with default_args(type=("build", "run")):
        depends_on("r-biocgenerics")
        depends_on("r-bslib")
        depends_on("r-data-table")
        depends_on("r-dplyr")
        depends_on("r-embedsom")
        depends_on("r-flowai")
        depends_on("r-flowcore@1.53.8:")
        depends_on("r-flowworkspace@3.35.8:")
        depends_on("r-gtools")
        depends_on("r-magrittr")
        depends_on("r-mass")
        depends_on("r-opencyto@1.25.2:")
        depends_on("r-purrr")
        depends_on("r-robustbase")
        depends_on("r-rhandsontable@0.3.7:")
        depends_on("r-rsvd")
        depends_on("r-rtsne")
        depends_on("r-shiny")
        depends_on("r-superheat@1.0.0:")
        depends_on("r-tibble")
        depends_on("r-tidyr")
        depends_on("r-umap")
        depends_on("r-visnetwork")

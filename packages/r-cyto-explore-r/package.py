# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-cyto-explore-r
#
# You can edit this file again by typing:
#
#     spack edit r-cyto-explore-r
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RCytoExploreR(RPackage):
    """Interactive Analysis of Cytometry Data.

    CytoExploreR provides an intuitive and interactive approach to analysing
    cytometry data in R, integrating conventional and cutting-edge tools under
    a unified, open-source framework.
    """

    homepage = "https://github.com/DillonHammill/CytoExploreR"
    git = "https://github.com/DillonHammill/CytoExploreR.git"

    maintainers("softpack-bot")

    license("GPL-2.0-only")

    # Legacy date-based snapshot
    version("20230228", commit="0efb1cc19fc701ae03905cf1b8484c1dfeb387df")
    # Newer 2.x line (was in r-cytoexplorer)
    version("2.0.15", commit="69088a6c5955afb2a2576c63e162de11ded7a882", preferred=True)

    depends_on("r@3.5.0:", type=("build", "run"), when="@2.0.15")

    # Depends / Imports from DESCRIPTION for 2.x
    with default_args(type=("build", "run")):
        depends_on("r-flowcore@2.3:", when="@2.0.15")
        depends_on("r-flowworkspace@4.3.1:", when="@2.0.15")
        depends_on("r-opencyto@1.25.2:", when="@2.0.15")

        depends_on("r-biocgenerics", when="@2.0.15")
        depends_on("r-bslib", when="@2.0.15")
        depends_on("r-data-table", when="@2.0.15")
        depends_on("r-dataeditr@0.1.2:", when="@2.0.15")
        depends_on("r-dplyr", when="@2.0.15")
        depends_on("r-future", when="@2.0.15")
        depends_on("r-future-apply", when="@2.0.15")
        depends_on("r-kernsmooth", when="@2.0.15")
        depends_on("r-mass", when="@2.0.15")
        depends_on("r-progress", when="@2.0.15")
        depends_on("r-purrr", when="@2.0.15")
        depends_on("r-heatmapr", when="@2.0.15")
        depends_on("r-reticulate", when="@2.0.15")
        depends_on("r-robustbase", when="@2.0.15")
        depends_on("r-rhandsontable@0.3.8:", when="@2.0.15")
        depends_on("r-shiny", when="@2.0.15")
        depends_on("r-tidyr", when="@2.0.15")
        depends_on("r-visnetwork", when="@2.0.15")
        depends_on("r-xml", when="@2.0.15")
        depends_on("r-rcpp", when="@2.0.15")  # Also in LinkingTo

    # Dependencies for the legacy snapshot release
    depends_on("r-flowcore", type=("build", "run"), when="@20230228")
    depends_on("r-flowworkspace", type=("build", "run"), when="@20230228")
    depends_on("r-opencyto", type=("build", "run"), when="@20230228")
    depends_on("r-biocgenerics", type=("build", "run"), when="@20230228")
    depends_on("r-bslib", type=("build", "run"), when="@20230228")
    depends_on("r-data-table", type=("build", "run"), when="@20230228")
    depends_on("r-dplyr", type=("build", "run"), when="@20230228")
    depends_on("r-embedsom", type=("build", "run"), when="@20230228")
    depends_on("r-flowai", type=("build", "run"), when="@20230228")
    depends_on("r-gtools", type=("build", "run"), when="@20230228")
    depends_on("r-mass", type=("build", "run"), when="@20230228")
    depends_on("r-magrittr", type=("build", "run"), when="@20230228")
    depends_on("r-purrr", type=("build", "run"), when="@20230228")
    depends_on("r-robustbase", type=("build", "run"), when="@20230228")
    depends_on("r-rhandsontable", type=("build", "run"), when="@20230228")
    depends_on("r-rtsne", type=("build", "run"), when="@20230228")
    depends_on("r-rsvd", type=("build", "run"), when="@20230228")
    depends_on("r-shiny", type=("build", "run"), when="@20230228")
    depends_on("r-superheat", type=("build", "run"), when="@20230228")
    depends_on("r-tibble", type=("build", "run"), when="@20230228")
    depends_on("r-tidyr", type=("build", "run"), when="@20230228")
    depends_on("r-umap", type=("build", "run"), when="@20230228")
    depends_on("r-visnetwork", type=("build", "run"), when="@20230228")
    depends_on("r-cyto-explore-r-data", type=("build", "run"), when="@20230228")

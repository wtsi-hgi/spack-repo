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
    """CytoExploreR is comprehensive collection of interactive exploratory cytometry analysis tools designed under a unified framework. CytoExploreR has been specifically designed to integrate all existing cytometry analysis techniques (e.g. manual gating, automated gating and dimension reduction) in a format that makes these tools freely accessible to users with no coding experience."""

    homepage = "https://github.com/DillonHammill/CytoExploreR"
    git = "https://github.com/DillonHammill/CytoExploreR.git"
    
    version("20230228", commit="0efb1cc19fc701ae03905cf1b8484c1dfeb387df")

    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowworkspace", type=("build", "run"))
    depends_on("r-opencyto", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-bslib", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-embedsom", type=("build", "run"))
    depends_on("r-flowai", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-robustbase", type=("build", "run"))
    depends_on("r-rhandsontable", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-rsvd", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-superheat", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-umap", type=("build", "run"))
    depends_on("r-visnetwork", type=("build", "run"))
    depends_on("r-cyto-explore-r-data", type=("build", "run"))



# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGa4ghshiny(RPackage):
    """Shiny application for interacting with GA4GH-based data servers

    GA4GHshiny package provides an easy way to interact with data servers based on Global Alliance for Genomics and Health (GA4GH) genomics API through a Shiny application. It also integrates with Beacon Network.
    """

    homepage = "https://github.com/labbcb/GA4GHshiny"
    bioc = "GA4GHshiny"

    version("1.30.0", commit="021b0c3b3f9b1ae68334b5fdb4ab3958b1c7df18")
    version("1.24.0", commit="705e6f3a14039ffef2a1c76bd053625d2859a0e3")

    depends_on("r-ga4ghclient", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-shinythemes", type=("build", "run"))

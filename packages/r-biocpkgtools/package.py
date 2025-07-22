# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocpkgtools(RPackage):
    """Collection of simple tools for learning about Bioconductor Packages

    Bioconductor has a rich ecosystem of metadata around packages, usage, and build status. This package is a simple collection of functions to access that metadata from R. The goal is to expose metadata for data mining and value-added functionality such as package searching, text mining, and analytics on packages.
    """

    homepage = "https://github.com/seandavi/BiocPkgTools"
    bioc = "BiocPkgTools"

    version("1.26.2", commit="c5f81824c37094750ede1a898882f91284d4ce97")
    version("1.20.0", commit="d7d15a34ef0826ec18de63da68d82e312d1f8f51")

    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-biocviews", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-rvest", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-gh", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rorcid", type=("build", "run"))
    depends_on("r-lubridate", type=("build", "run"))

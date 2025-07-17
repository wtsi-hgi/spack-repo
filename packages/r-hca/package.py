# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHca(RPackage):
    """Exploring the Human Cell Atlas Data Coordinating Platform

    This package provides users with the ability to query the Human Cell Atlas data repository for single-cell experiment data. The `projects()`, `files()`, `samples()` and `bundles()` functions retrieve summary information on each of these indexes; corresponding `*_details()` are available for individual entries of each index. File-based resources can be downloaded using `files_download()`. Advanced use of the package allows the user to page through large result sets, and to flexibly query the 'list-of-lists' structure representing query responses.
    """

    bioc = "hca"

    version("1.16.0", commit="3c99355091b42e7934830832c617303a1749c15a")
    version("1.10.1", commit="7189c1b574529be1dce8b488bb43ba8896282d2d")
    version("1.10.0", md5="8a1c812efb51ab7e30a7d419bdf918a3")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-miniui", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))

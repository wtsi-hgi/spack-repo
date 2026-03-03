# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrsampleoverlap(RPackage):
    """Estimate Bias Due To Sample Overlap In Mendelian Randomization Studies"""

    homepage = "https://github.com/mglev1n/mrSampleOverlap"
    git = "https://github.com/mglev1n/mrSampleOverlap.git"

    license("MIT")

    version("20220901", commit="e59d2794c7c0097081bcd4a0d960aded4ef4a9ca")

    # Required dependencies (from Imports)
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyverse", type=("build", "run"))
    depends_on("r-twosamplemr", type=("build", "run"))

    # Suggested dependencies (from Suggests)
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run")) 
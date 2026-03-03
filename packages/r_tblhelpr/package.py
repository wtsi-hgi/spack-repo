# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTblhelpr(RPackage):
    """Functions for common operations on tidyverse tibbles, for example
    allowing conversion to matrices, calculation of PCA or tSNE and adding 
    hclust ordering to factor columns."""

    homepage = "https://github.com/allydunham/tblhelpr"
    git = "https://github.com/allydunham/tblhelpr.git"

    license("LGPL-3.0")

    version("20191118", commit="5b42bd0ac34cde921e71e69ad40e1701075034a0")

    depends_on("r@3.5.0:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))

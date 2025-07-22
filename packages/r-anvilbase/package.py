# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnvilbase(RPackage):
    """Base package for AnVIL functionality

    This package provides base functionality for the AnVIL (Analysis, Visualization, and Informatics Lab-space) platform.
    """

    bioc = "AnVILBase"
    version("1.2.0", commit="446496443716280db9a1efa0365ff169d083ac8d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-httr2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run")) 
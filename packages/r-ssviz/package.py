# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsviz(RPackage):
    """A small RNA-seq visualizer and analysis toolkit

    Small RNA sequencing viewer
    """

    bioc = "ssviz"

    version("1.42.0", commit="44a6677242e7dca29b3f03c504c753c8558a656a")
    version("1.36.0", commit="18260e5f4a9c10971f15c01a9d60678ffd8f5e28")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))

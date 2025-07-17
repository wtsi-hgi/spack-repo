# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfp(RPackage):
    """Gene Selection

    This package provides a supervised technique able to identify differentially expressed genes, based on the construction of emph{Fuzzy Patterns} (FPs). The Fuzzy Patterns are built by means of applying 3 Membership Functions to discretized gene expression values.
    """

    bioc = "DFP"

    version("1.66.0", commit="99063a724f5eee62f8ac9ac3ada1a9a6fc82313f")
    version("1.60.0", commit="850ddadfd19f69af83c01f1fdf69cc94c4aa6023")

    depends_on("r-biobase@2.5.5:", type=("build", "run"))

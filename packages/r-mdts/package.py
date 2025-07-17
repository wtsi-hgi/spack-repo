# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdts(RPackage):
    """Detection of de novo deletion in targeted sequencing trios

    A package for the detection of de novo copy number deletions in targeted sequencing of trios with high sensitivity and positive predictive value.
    """

    bioc = "MDTS"

    version("1.28.0", commit="2078f3e79273dab1abd3b589656957addcf32692")
    version("1.22.0", commit="7791f1ee8761f37ff6fc6adf26c990c024a6c7db")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-dnacopy", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))

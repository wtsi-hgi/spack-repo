# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynextend(RPackage):
    """Tools for Working With Synteny Objects

    Shared order between genomic sequences provide a great deal of information. Synteny objects produced by the R package DECIPHER provides quantitative information about that shared order. SynExtend provides tools for extracting information from Synteny objects.
    """

    bioc = "SynExtend"

    version("1.20.2", commit="6d3d7fc30a7b0893fa494ad3d495e0b34f657467")
    version("1.14.0", commit="ac9587f1b719bca8b8ed6e2398c670f34bc85ab6")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-decipher@2.28:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))

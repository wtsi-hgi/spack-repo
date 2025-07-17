# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBadregionfinder(RPackage):
    """BadRegionFinder: an R/Bioconductor package for identifying regions with bad coverage

    BadRegionFinder is a package for identifying regions with a bad, acceptable and good coverage in sequence alignment data available as bam files. The whole genome may be considered as well as a set of target regions. Various visual and textual types of output are available.
    """

    bioc = "BadRegionFinder"

    version("1.36.0", commit="0f424a2ce19082db3d69a2cedf09760c07cc4ffb")
    version("1.30.0", commit="b58606fbe768431017deac8c05a83363d7ad826b")

    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

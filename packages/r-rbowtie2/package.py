# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbowtie2(RPackage):
    """An R Wrapper for Bowtie2 and AdapterRemoval

    This package provides an R wrapper of the popular bowtie2 sequencing reads aligner and AdapterRemoval, a convenient tool for rapid adapter trimming, identification, and read merging. The package contains wrapper functions that allow for genome indexing and alignment to those indexes. The package also allows for the creation of .bam files via Rsamtools.
    """

    bioc = "Rbowtie2"

    version("2.14.0", commit="ca8379016316bcc73e743efef80ef512dfc0ee73")
    version("2.8.0", commit="34c5114d84e7e0781e98bbc26e44f9606335a99f")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("samtools", type=("build", "link", "run"))
    depends_on("zlib", type=("build", "link", "run"))

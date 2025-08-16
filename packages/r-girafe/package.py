# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGirafe(RPackage):
    """Genome Intervals and Read Alignments for Functional Exploration

    The package 'girafe' deals with the genome-level representation of aligned reads from next-generation sequencing data. It contains an object class for enabling a detailed description of genome intervals with aligned reads and functions for comparing, visualising, exporting and working with such intervals and the aligned reads. As such, the package interacts with and provides a link between the packages ShortRead, IRanges and genomeIntervals.
    """

    bioc = "girafe"

    version("1.60.0", commit="1e8b0ed80903b3d7c036cdb145fadcc4a75b8c7b")
    version("1.54.0", commit="15a75307f41799f6a75b05d8aec996653093339f")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
    depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
    depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
    depends_on("r-intervals@0.13.1:", type=("build", "run"))
    depends_on("r-shortread@1.37.1:", type=("build", "run"))
    depends_on("r-genomeintervals@1.25.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biostrings@2.47.6:", type=("build", "run"))
    depends_on("r-iranges@2.13.12:", type=("build", "run"))
    # Added missing dependency required by recent Bioconductor releases
    depends_on("r-pwalign", type=("build", "run"))

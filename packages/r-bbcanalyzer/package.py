# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbcanalyzer(RPackage):
    """BBCAnalyzer: an R/Bioconductor package for visualizing base counts

    BBCAnalyzer is a package for visualizing the relative or absolute number of bases, deletions and insertions at defined positions in sequence alignment data available as bam files in comparison to the reference bases. Markers for the relative base frequencies, the mean quality of the detected bases, known mutations or polymorphisms and variants called in the data may additionally be included in the plots.
    """

    bioc = "BBCAnalyzer"

    version("1.38.0", commit="2a67e491e3f6fd45d1468b5e309c547e41ad0212")
    version("1.32.0", commit="eb90d95859efcf397a5a43b23dfd5cd4147f79b3")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))

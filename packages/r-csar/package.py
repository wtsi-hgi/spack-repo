# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsar(RPackage):
    """Statistical tools for the analysis of ChIP-seq data

    Statistical tools for ChIP-seq data analysis. The package includes the statistical method described in Kaufmann et al. (2009) PLoS Biology: 7(4):e1000090. Briefly, Taking the average DNA fragment size subjected to sequencing into account, the software calculates genomic single-nucleotide read-enrichment values. After normalization, sample and control are compared using a test based on the Poisson distribution. Test statistic thresholds to control the false discovery rate are obtained through random permutation.
    """

    bioc = "CSAR"

    version("1.60.0", commit="104d0ff6629333cd249c9c8860cc124306b2a843")
    version("1.54.0", commit="e73960078e8b261a4bd7ee0bb356a7ef9a2d4345")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))

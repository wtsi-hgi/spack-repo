# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiboprofiling(RPackage):
    """Ribosome Profiling Data Analysis: from BAM to Data Representation and Interpretation

    Starting with a BAM file, this package provides the necessary functions for quality assessment, read start position recalibration, the counting of reads on CDS, 3'UTR, and 5'UTR, plotting of count data: pairs, log fold-change, codon frequency and coverage assessment, principal component analysis on codon coverage.
    """

    bioc = "RiboProfiling"

    version("1.38.0", commit="11b44e26eae5d757ba3d842740d86080bc87c4e3")
    version("1.32.0", commit="8cec7bfdb5bd227c6485ba85b566c47d71db5557")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-sqldf", type=("build", "run"))

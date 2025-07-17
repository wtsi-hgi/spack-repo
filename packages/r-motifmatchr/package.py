# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifmatchr(RPackage):
    """Fast Motif Matching in R

    Quickly find motif matches for many motifs and many sequences. Wraps C++ code from the MOODS motif calling library, which was developed by Pasi Rastas, Janne Korhonen, and Petri Martinmäki.
    """

    bioc = "motifmatchr"

    version("1.30.0", commit="662d8246ff8502055206fe10fac0b99f45092e0b")
    version("1.24.0", commit="40511431be263ede54e0151e578bfe5f35ed98e9")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-tfbstools", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))

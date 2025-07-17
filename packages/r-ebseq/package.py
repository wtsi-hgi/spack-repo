# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbseq(RPackage):
    """An R package for gene and isoform differential expression analysis of RNA-seq data

    Differential Expression analysis at both gene and isoform level using RNA-seq data
    """

    bioc = "EBSeq"

    version("2.6.0", commit="c4e5f5a2570923d75efd6c026bd248721f207c8e")
    version("2.0.0", commit="f1d4e4419988ab98540739c9349559fd437cb59f")

    depends_on("r-blockmodeling", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r@3:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))

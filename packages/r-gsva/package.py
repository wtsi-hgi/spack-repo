# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsva(RPackage):
    """Gene Set Variation Analysis for Microarray and RNA-Seq Data

    Gene Set Variation Analysis (GSVA) is a non-parametric, unsupervised method for estimating variation of gene set enrichment through the samples of a expression data set. GSVA performs a change in coordinate systems, transforming the data from a gene by sample matrix to a gene-set by sample matrix, thereby allowing the evaluation of pathway enrichment for each sample. This new matrix of GSVA enrichment scores facilitates applying standard analytical methods like functional enrichment, survival analysis, clustering, CNV-pathway analysis or cross-tissue pathway analysis, in a pathway-centric manner.
    """

    homepage = "https://github.com/rcastelo/GSVA"
    bioc = "GSVA"

    version("2.2.0", commit="619f08d1de6de67f6f283d4350e66ee40159aab1")
    version("1.50.1", md5="6412f61594abfb970a54869bfd48a9a0")
    version("1.50.0", md5="e21af1ab9dabfa5801fb978b50f992e2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-matrix@1.5.0:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-sparsematrixstats", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsimseq(RPackage):
    """Semi-parametric simulation tool for bulk and single-cell RNA sequencing data

    SPsimSeq uses a specially designed exponential family for density estimation to constructs the distribution of gene expression levels from a given real RNA sequencing data (single-cell or bulk), and subsequently simulates a new dataset from the estimated marginal distributions using Gaussian-copulas to retain the dependence between genes. It allows simulation of multiple groups and batches with any required sample size and library size.
    """

    homepage = "https://github.com/CenterForStatistics-UGent/SPsimSeq"
    bioc = "SPsimSeq"

    version("1.18.0", commit="807cebe3ee8934f3ff43246e5c2a672f85ff98c3")
    version("1.12.0", commit="e2487910baf119b6b186609e3f316f157ea0d9f7")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-fitdistrplus", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-phyloseq", type=("build", "run"))

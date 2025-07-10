# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmet(RPackage):
	"""Bayesian modelling of cell-to-cell DNA methylation heterogeneity

	High-throughput single-cell measurements of DNA methylomes can quantify methylation heterogeneity and uncover its role in gene regulation. However, technical limitations and sparse coverage can preclude this task. scMET is a hierarchical Bayesian model which overcomes sparsity, sharing information across cells and genomic features to robustly quantify genuine biological heterogeneity. scMET can identify highly variable features that drive epigenetic heterogeneity, and perform differential methylation and variability analyses. We illustrate how scMET facilitates the characterization of epigenetically distinct cell populations and how it enables the formulation of novel hypotheses on the epigenetic regulation of gene expression.
	"""
	
	bioc = "scMET" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scMET_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scMET/scMET_1.4.0.tar.gz"]

	version("1.4.0", sha256="b4908e98a14b2a3ed26b52648a5ae025711676d8d06ad30a16bbfd0cc5007f2a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.21.3:", type=("build", "run"))
	depends_on("r-rstantools@2.1:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-logitnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.21.0.7:", type=("build", "run"))

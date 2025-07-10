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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SPsimSeq_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SPsimSeq/SPsimSeq_1.12.0.tar.gz"]

	version("1.12.0", sha256="164769088f5a29ec68459cbacc99a101dfd2195d407dca823f95fafe1b34d031")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))

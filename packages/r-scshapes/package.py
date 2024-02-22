# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScshapes(RPackage):
	"""A Statistical Framework for Modeling and Identifying Differential Distributions in Single-cell RNA-sequencing Data

	We present a novel statistical framework for identifying differential distributions in single-cell RNA-sequencing (scRNA-seq) data between treatment conditions by modeling gene expression read counts using generalized linear models (GLMs). We model each gene independently under each treatment condition using error distributions Poisson (P), Negative Binomial (NB), Zero-inflated Poisson (ZIP) and Zero-inflated Negative Binomial (ZINB) with log link function and model based normalization for differences in sequencing depth. Since all four distributions considered in our framework belong to the same family of distributions, we first perform a Kolmogorov-Smirnov (KS) test to select genes belonging to the family of ZINB distributions. Genes passing the KS test will be then modeled using GLMs. Model selection is done by calculating the Bayesian Information Criterion (BIC) and likelihood ratio test (LRT) statistic.
	"""
	
	homepage = "https://github.com/Malindrie/scShapes"
	bioc = "scShapes" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scShapes_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scShapes/scShapes_1.8.0.tar.gz"]

	version("1.8.0", md5="5a4954c320f7b1f30f8fbff6e9f5ad91")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-dgof", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

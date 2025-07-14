# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmsparsenet(RPackage):
	"""Network Centrality Metrics for Elastic-Net Regularized Models

	glmSparseNet is an R-package that generalizes sparse regression models when the features (e.g. genes) have a graph structure (e.g. protein-protein interactions), by including network-based regularizers.  glmSparseNet uses the glmnet R-package, by including centrality measures of the network as penalty weights in the regularization. The current version implements regularization based on node degree, i.e. the strength and/or number of its associated edges, either by promoting hubs in the solution or orphan genes in the solution. All the glmnet distribution families are supported, namely "gaussian", "poisson", "binomial", "multinomial", "cox", and "mgaussian".
	"""
	
	homepage = "https://www.github.com/sysbiomed/glmSparseNet"
	bioc = "glmSparseNet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/glmSparseNet_1.20.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/glmSparseNet/glmSparseNet_1.20.1.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.1", sha256="34d13f31513386993fb5b88433c2b48e6f7ee457498a7a477b9727c984519525")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-futile-options", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))

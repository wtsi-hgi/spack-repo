# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContext(RPackage):
	"""'a la Carte' on Text (ConText) Embedding Regression

	A fast, flexible and transparent framework to estimate context-specific word and short document embeddings using the 'a la carte' 
    embeddings approach developed by Khodak et al. (2018) <arXiv:1805.05388> and evaluate hypotheses about covariate effects on embeddings using 
    the regression framework developed by Rodriguez et al. (2021)<https://github.com/prodriguezsosa/EmbeddingRegression>.
	"""
	
	homepage = "https://github.com/prodriguezsosa/EmbeddingRegression"
	cran = "conText" 

	version("1.4.3", md5="772c1dd334dbe6691f1eb1184b983e0c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix@1.3.2:", type=("build", "run"))
	depends_on("r-quanteda@3:", type=("build", "run"))
	depends_on("r-text2vec@0.6:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

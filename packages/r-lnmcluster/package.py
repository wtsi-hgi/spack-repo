# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLnmcluster(RPackage):
	"""Perform Logistic Normal Multinomial Clustering for Microbiome
Compositional Data

	An implementation of logistic normal multinomial (LNM) clustering. It is an extension of LNM mixture model proposed by Fang and Subedi (2020) <arXiv:2011.06682>, and is designed for clustering compositional data. The package includes 3 extended models: LNM Factor Analyzer (LNM-FA), LNM Bicluster Mixture Model (LNM-BMM) and Penalized LNM Factor Analyzer (LNM-FA). There are several advantages of LNM models: 1. LNM provides more flexible covariance structure; 2. Factor analyzer can reduce the number of parameters to estimate; 3. Bicluster can simultaneously cluster subjects and taxa, and provides significant biological insights; 4. Penalty term allows sparse estimation in the covariance matrix. Details for model assumptions and interpretation can be found in papers: Tu and Subedi (2021) <arXiv:2101.01871> and Tu and Subedi (2022) <doi:10.1002/sam.11555>.  
	"""
	
	cran = "lnmCluster" 

	version("0.3.1", md5="03f7ec039bc0a2766779fe95706bd8f7")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pgmm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

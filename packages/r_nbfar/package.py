# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbfar(RPackage):
	"""Negative Binomial Factor Regression Models ('nbfar')

	We developed a negative binomial factor regression model to estimate structured (sparse) associations between a feature matrix X and overdispersed count data Y.  With 'nbfar', microbiome count data Y can be used, for example, to associate host or environmental covariates with microbial abundances. Currently, two models are available: a) Negative Binomial reduced rank regression (NB-RRR), b) Negative Binomial co-sparse factor regression (NB-FAR). Please refer the manuscript 'Mishra, A. K., & Müller, C. L. (2021). Negative Binomial factor regression with application to microbiome data analysis. bioRxiv.' for more details. 
	"""
	
	homepage = "https://github.com/amishra-stats/nbfar"
	cran = "nbfar" 

	version("0.1", md5="a71955ea14b9b03e0e68f607cf63a5c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rrpack", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-mpath", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

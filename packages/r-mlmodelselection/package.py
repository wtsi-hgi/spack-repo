# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmodelselection(RPackage):
	"""Model Selection in Multivariate Longitudinal Data Analysis

	An efficient Gibbs sampling algorithm is developed for Bayesian multivariate longitudinal data analysis with the focus on selection of important elements in the generalized autoregressive matrix. It provides posterior samples and estimates of parameters. In addition, estimates of several information criteria such as Akaike information criterion (AIC), Bayesian information criterion (BIC), deviance information criterion (DIC) and prediction accuracy such as the marginal predictive likelihood (MPL) and the mean squared prediction error (MSPE) are provided for model selection. 
	"""
	
	homepage = "https://github.com/kuojunglee/"
	cran = "MLModelSelection" 

	version("1.0", md5="c796ef4031b1a0852884264a73d304d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMombf(RPackage):
	"""Model Selection with Bayesian Methods and Information Criteria

	Model selection and averaging for regression and mixtures, inclusing Bayesian model selection and information criteria (BIC, EBIC, AIC, GIC).
	"""
	
	homepage = "https://github.com/davidrusi/mombf"
	cran = "mombf" 

	version("3.5.4", md5="3325760f6c050e1f19df439d9bfed30c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

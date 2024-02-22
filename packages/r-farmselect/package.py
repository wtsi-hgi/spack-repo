# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarmselect(RPackage):
	"""Factor Adjusted Robust Model Selection

	Implements a consistent model selection strategy for high dimensional sparse regression when the covariate dependence can be reduced through factor models. By separating the latent factors from idiosyncratic components, the problem is transformed from model selection with highly correlated covariates to that with weakly correlated variables. It is appropriate for cases where we have many variables compared to the number of samples. Moreover, it implements a robust procedure to estimate distribution parameters wherever possible, hence being suitable for cases when the underlying distribution deviates from Gaussianity. See the paper on the 'FarmSelect' method, Fan et al.(2017) <arXiv:1612.08490>, for detailed description of methods and further references. 
	"""
	
	homepage = "https://kbose28.github.io/FarmSelect/"
	cran = "FarmSelect" 

	version("1.0.2", md5="f7edecf50bb46cac49d4ab7dd8f80db5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

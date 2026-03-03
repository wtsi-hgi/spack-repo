# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiridge(RPackage):
	"""Fast Cross-Validation for Multi-Penalty Ridge Regression

	Multi-penalty linear, logistic and cox ridge regression, including estimation of the penalty parameters by efficient (repeated) cross-validation and marginal likelihood maximization. Multiple high-dimensional data types that require penalization are allowed, as well as unpenalized variables. Paired and preferential data types can be specified. See Van de Wiel et al. (2021), <arXiv:2005.09301>. 
	"""
	
	cran = "multiridge" 

	version("1.11", md5="bc38eeacf995ce41faf6ba02793bff42")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))

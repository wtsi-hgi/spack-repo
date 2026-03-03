# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantreggrowth(RPackage):
	"""Non-Crossing Additive Regression Quantiles and Non-Parametric
Growth Charts

	Fits non-crossing regression quantiles as a function of linear covariates and multiple smooth terms, including varying coefficients, via B-splines with L1-norm difference penalties.  
    Random intercepts and variable selection are allowed via the lasso penalties.
    The smoothing parameters are estimated as part of the model fitting, see Muggeo and others (2021) <doi:10.1177/1471082X20929802>. Monotonicity and concavity 
    constraints on the fitted curves are allowed, see Muggeo and others (2013) <doi:10.1007/s10651-012-0232-1>, 
    and also <doi:10.13140/RG.2.2.12924.85122> or <doi:10.13140/RG.2.2.29306.21445> some code examples.
	"""
	
	cran = "quantregGrowth" 

	version("1.7-0", md5="7b4e65ba4da6246bc613c6cbb3d7143c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))

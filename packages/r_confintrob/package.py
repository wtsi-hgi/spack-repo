# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfintrob(RPackage):
	"""Bootstrap Confidence Intervals for Robust and Classical Linear
Mixed Model Estimators

	The main function calculates confidence intervals (CI) for Mixed Models, utilizing both classical estimators from the lmer() function in the 'lme4' package and robust estimators from the rlmer() function in the 'robustlmm' package, as well as the varComprob() function in the 'robustvarComp' package. Three methods are available: the classical Wald method, the wild bootstrap, and the parametric bootstrap. Bootstrap methods offer flexibility in obtaining lower and upper bounds through percentile or BCa methods. More details are given in n Mason, F., Cantoni, E., & Ghisletta, P. (2021) <doi:10.5964/meth.6607> and n Mason, F., Cantoni, E., & Ghisletta, P. (2024) <doi:10.1037/met0000643>.
	"""
	
	cran = "confintROB" 

	version("1.0", md5="8bb764af20fc28e5eef4f4d44e5df4ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

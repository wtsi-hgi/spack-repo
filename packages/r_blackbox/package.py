# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlackbox(RPackage):
	"""Black Box Optimization and Exploration of Parameter Space

	Performs prediction of a response function from simulated response values, allowing black-box optimization of functions estimated with some error. Includes a simple user interface for such applications, as well as more specialized functions designed to be called by the Migraine software (Rousset and Leblois, 2012 <doi:10.1093/molbev/MSR262>; Leblois et al., 2014 <doi:10.1093/molbev/msu212>; and see URL). The latter functions are used for prediction of likelihood surfaces and implied likelihood ratio confidence intervals, and for exploration of predictor space of the surface. Prediction of the response is based on ordinary Kriging (with residual error) of the input. Estimation of smoothing parameters is performed by generalized cross-validation.
	"""
	
	homepage = "https://kimura.univ-montp2.fr/~rousset/Migraine.htm"
	cran = "blackbox" 

	version("1.1.46", md5="3bf6bf7c90a5bb95a6f1cb91eff0ec9d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-geometry@0.3.6:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-spamm@3.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

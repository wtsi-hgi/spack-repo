# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPemultinom(RPackage):
	"""L1-Penalized Multinomial Regression with Statistical Inference

	We aim for fitting a multinomial regression model with Lasso penalty and doing statistical inference (calculating confidence intervals of coefficients and p-values for individual variables). It implements 1) the coordinate descent algorithm to fit an l1-penalized multinomial regression model (parameterized with a reference level); 2) the debiasing approach to obtain the inference results, which is described in Tian et al. (2023) <arXiv:2302.02310>.
	"""
	
	cran = "pemultinom" 

	version("0.1.0", md5="31e32c47564f37c7bc94b3f6ddd56ec1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

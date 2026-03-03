# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtrkernsmooth(RPackage):
	"""Estimate and Make Inference About Optimal Treatment Regimes via
Smoothed Methods

	Methods to estimate the optimal treatment regime among all linear regimes via smoothed estimation methods, and construct element-wise confidence intervals for the optimal linear treatment regime vector, as well as the confidence interval for the optimal value via wild bootstrap procedures, if the population follows treatments recommended by the optimal linear regime. See more details in: Wu, Y. and Wang, L. (2021), "Resampling-based Confidence Intervals for Model-free Robust Inference on Optimal Treatment Regimes", Biometrics, 77: 465– 476, <doi:10.1111/biom.13337>.
	"""
	
	cran = "DTRKernSmooth" 

	version("1.1.0", md5="4ecc1a7896781b6cceecff049647fe34")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

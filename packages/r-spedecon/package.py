# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpedecon(RPackage):
	"""Smoothness-Penalized Deconvolution for Density Estimation Under
Measurement Error

	Implements the Smoothness-Penalized Deconvolution method for estimating a probability density under measurement error of Kent and Ruppert (2023) <doi:10.1080/01621459.2023.2259028>. The estimator is formed by computing a histogram of the error-contaminated data, and then finding an estimate that minimizes a reconstruction error plus a smoothness-inducing penalty term. The primary function, sped(), takes the data and error distribution, and returns the estimator as a function.
	"""
	
	homepage = "https://www.davidjkent.org"
	cran = "spedecon" 

	version("0.1", md5="ee568a8ead8d3c6e17af68c6cb05a03d")

	depends_on("r-quadprog", type=("build", "run"))

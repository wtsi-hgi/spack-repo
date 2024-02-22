# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeyondwhittle(RPackage):
	"""Bayesian Spectral Inference for Time Series

	Implementations of Bayesian parametric, nonparametric and semiparametric procedures for univariate and multivariate time series. The package is based on the methods presented in C. Kirch et al (2018) <doi:10.1214/18-BA1126>, A. Meier (2018) <https://opendata.uni-halle.de//handle/1981185920/13470> and Y. Tang et al (2023) <arXiv:2303.11561>. It was supported by DFG grants KI 1443/3-1 and KI 1443/3-2.
	"""
	
	cran = "beyondWhittle" 

	version("1.2.0", md5="3fa631fa766f3a5c02a7c60e6f416ebd")

	depends_on("r-ltsa@1.4.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixr(RPackage):
	"""Finite Mixture Modeling for Raw and Binned Data

	Performs maximum likelihood estimation for finite mixture models for families including Normal, Weibull, Gamma and Lognormal by using EM algorithm, together with Newton-Raphson algorithm or bisection method when necessary. It also conducts mixture model selection by using information criteria or bootstrap likelihood ratio test. The data used for mixture model fitting can be raw data or binned data. The model fitting process is accelerated by using R package 'Rcpp'.
	"""
	
	cran = "mixR" 

	version("0.2.0", md5="53d12d1f35706dab35a6ef42b6512c3b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

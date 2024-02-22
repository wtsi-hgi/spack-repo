# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimode(RPackage):
	"""Statistical Inference for Systems of Ordinary Differential
Equations using Separable Integral-Matching

	Implements statistical inference for systems of ordinary differential equations,
  that uses the integral-matching criterion and takes advantage of the separability of parameters,
  in order to obtain initial parameter estimates for nonlinear least squares optimization. 
  Dattner & Yaari (2018) <arXiv:1807.04202>. 
  Dattner et al. (2017) <doi:10.1098/rsif.2016.0525>.
  Dattner & Klaassen (2015) <doi:10.1214/15-EJS1053>.
	"""
	
	cran = "simode" 

	version("1.2.2", md5="1ea5d6bc475d29d0dff6bd5a4af466c5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))

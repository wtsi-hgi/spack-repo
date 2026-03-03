# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeakarma(RPackage):
	"""Tools for the Analysis of Weak ARMA Models

	Numerous time series admit autoregressive moving average (ARMA)
  representations, in which the errors are uncorrelated but not necessarily
  independent.
  These models are called weak ARMA by opposition to the standard ARMA models, 
  also called strong ARMA models, in which the error terms are supposed to be 
  independent and identically distributed (iid).
  This package allows the study of nonlinear time series models through weak 
  ARMA representations.
  It determines identification, estimation and validation for ARMA models and 
  for AR and MA models in particular. 
  Functions can also be used in the strong case.
  This package also works on white noises by omitting arguments 'p', 'q', 'ar'
  and 'ma'.
  See Francq, C. and Zakoïan, J. (1998) <doi:10.1016/S0378-3758(97)00139-0> and 
  Boubacar Maïnassara, Y. and Saussereau, B. (2018)
  <doi:10.1080/01621459.2017.1380030> for more details.
	"""
	
	homepage = "https://plmlab.math.cnrs.fr/jrolland/weakARMA"
	cran = "weakARMA" 

	version("1.0.3", md5="f892d8adb2dd06d5185525598f415a1d")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-compquadform@1.4.3:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-matrixstats@0.61:", type=("build", "run"))
	depends_on("r-vars@1.5.6:", type=("build", "run"))

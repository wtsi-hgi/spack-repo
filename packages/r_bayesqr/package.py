# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesqr(RPackage):
	"""Bayesian Quantile Regression

	Bayesian quantile regression using the asymmetric Laplace distribution, both continuous as well as binary dependent variables are supported. The package consists of implementations of the methods of Yu & Moyeed (2001) <doi:10.1016/S0167-7152(01)00124-9>, Benoit & Van den Poel (2012) <doi:10.1002/jae.1216> and Al-Hamzawi, Yu & Benoit (2012) <doi:10.1177/1471082X1101200304>. To speed up the calculations, the Markov Chain Monte Carlo core of all algorithms is programmed in Fortran and called from R.
	"""
	
	cran = "bayesQR" 

	version("2.4", md5="fd69cf1e31b14ad8fa22e922d5de7070")

	depends_on("r@4.2:", type=("build", "run"))

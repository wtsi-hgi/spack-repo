# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustgasp(RPackage):
	"""Robust Gaussian Stochastic Process Emulation

	Robust parameter estimation and prediction of Gaussian stochastic 
 process emulators. It allows for robust parameter estimation and prediction using 
 Gaussian stochastic process emulator. It also implements the parallel partial 
 Gaussian stochastic process emulator for computer model with massive outputs 
 See the reference: Mengyang Gu and Jim Berger, 2016, Annals of Applied Statistics; 
 Mengyang Gu, Xiaojing Wang and Jim Berger, 2018, Annals of Statistics. 
	"""
	
	cran = "RobustGaSP" 

	version("0.6.6", md5="2efa05124715225826def01b9c28be50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr@1.0.4:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

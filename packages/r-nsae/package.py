# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsae(RPackage):
	"""Nonstationary Small Area Estimation

	Executes nonstationary Fay-Herriot model and nonstationary generalized linear mixed model for small area estimation.The empirical best linear unbiased predictor (EBLUP) under stationary and nonstationary Fay-Herriot models and empirical best predictor (EBP) under nonstationary generalized linear mixed model along with the mean squared error estimation are included. EBLUP for prediction of non-sample area is also included under both stationary and nonstationary Fay-Herriot models. This extension to the Fay-Herriot model that accounts for the presence  of spatial nonstationarity was developed by Hukum Chandra, Nicola Salvati and Ray Chambers (2015) <doi:10.1093/jssam/smu026> and nonstationary generalized linear mixed model was developed by Hukum  Chandra, Nicola Salvati and Ray Chambers (2017) <doi:10.1016/j.spasta.2017.01.004>. This package is dedicated to the memory of Dr. Hukum Chandra who passed away while the package creation was in progress.
	"""
	
	cran = "NSAE" 

	version("0.4.0", md5="584897a7ceb2809fe1db883b42a7f54a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-spgwr", type=("build", "run"))
	depends_on("r-semipar", type=("build", "run"))

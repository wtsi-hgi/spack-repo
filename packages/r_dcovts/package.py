# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcovts(RPackage):
	"""Distance Covariance and Correlation for Time Series Analysis

	Computing and plotting the distance covariance and correlation function of a univariate or a multivariate time series. Both versions of biased and unbiased estimators of distance covariance and correlation are provided. Test statistics for testing pairwise independence are also implemented. Some data sets are also included. References include: 
			       a) Edelmann Dominic, Fokianos Konstantinos and Pitsillou Maria (2019). 'An Updated Literature Review of Distance Correlation and Its Applications to Time Series'. International Statistical Review, 87(2): 237--262. <doi:10.1111/insr.12294>.
             b) Fokianos Konstantinos and Pitsillou Maria (2018). 'Testing independence for multivariate time series via the auto-distance correlation matrix'. Biometrika, 105(2): 337--352. <doi:10.1093/biomet/asx082>.
             c) Fokianos Konstantinos and Pitsillou Maria (2017). 'Consistent testing for pairwise dependence in time series'. Technometrics, 59(2): 262--270. <doi:10.1080/00401706.2016.1156024>.
             d) Pitsillou Maria and Fokianos Konstantinos (2016). 'dCovTS: Distance Covariance/Correlation for Time Series'. R Journal, 8(2):324-340. <doi:10.32614/RJ-2016-049>.
	"""
	
	cran = "dCovTS" 

	version("1.4", md5="64aaf37a6cbf0a1106bc34d2a4c4b634")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dcov", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))

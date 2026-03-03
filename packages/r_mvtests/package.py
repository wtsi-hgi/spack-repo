# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvtests(RPackage):
	"""Multivariate Hypothesis Tests

	Multivariate hypothesis tests and the confidence intervals. It can be used to test the hypothesizes about mean vector or vectors (one-sample, two independent samples, paired samples), covariance matrix (one or more matrices), and the correlation matrix. Moreover, it can be used for robust Hotelling T^2 test at one sample case in high dimensional data. For this package, we have benefited from the studies Rencher (2003), Nel and Merwe (1986) <DOI: 10.1080/03610928608829342>, Tatlidil (1996), Tsagris (2014), Villasenor Alva and Estrada (2009) <DOI: 10.1080/03610920802474465>.
	"""
	
	cran = "MVTests" 

	version("2.2.2", md5="6f6ea1eea6206e47c88f33cea89cae75")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))

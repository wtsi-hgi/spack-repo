# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaebnocov(RPackage):
	"""Small Area Estimation using Empirical Bayes without Auxiliary
Variable

	Estimates the parameter of small area in binary data without
             auxiliary variable using Empirical Bayes technique, mainly from Rao 
             and Molina (2015,ISBN:9781118735787) with book entitled "Small Area Estimation Second Edition". 
             This package provides another option of direct estimation using weight.
             This package also features alpha and beta parameter estimation on calculating process of small area.
             Those methods are Newton-Raphson and Moment which based on Wilcox (1979) <doi:10.1177/001316447903900302> 
             and Kleinman (1973) <doi:10.1080/01621459.1973.10481332>.
	"""
	
	cran = "saebnocov" 

	version("0.1.0", md5="2e49807439b898a7352c529880bb5b2f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-descr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

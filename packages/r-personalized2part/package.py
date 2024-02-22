# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersonalized2part(RPackage):
	"""Two-Part Estimation of Treatment Rules for Semi-Continuous Data

	Implements the methodology of Huling, Smith, and 
    Chen (2020) <doi:10.1080/01621459.2020.1801449>, which allows for subgroup identification 
    for semi-continuous outcomes by estimating individualized treatment rules. It uses a two-part 
    modeling framework to handle semi-continuous data by separately modeling the positive part 
    of the outcome and an indicator of whether each outcome is positive, but still results in a 
    single treatment rule. High dimensional data is handled with a cooperative lasso penalty, 
    which encourages the coefficients in the two models to have the same sign. 
	"""
	
	homepage = "https://github.com/jaredhuling/personalized2part"
	cran = "personalized2part" 

	version("0.0.1", md5="cfa05fbde826acde5445ccb59503bcbb")

	depends_on("r-personalized", type=("build", "run"))
	depends_on("r-hdtweedie", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

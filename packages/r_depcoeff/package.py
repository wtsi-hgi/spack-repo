# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepcoeff(RPackage):
	"""Dependency Coefficients

	Functions to compute coefficients measuring the dependence of two or more than two variables. The functions can be deployed to gain information about functional dependencies of the variables with emphasis on monotone functions. The statistics describe how well one response variable can be approximated by a monotone function of other variables. In regression analysis the variable selection is an important issue. In this framework the functions could be useful tools in modeling the regression function. Detailed explanations on the subject can be found in papers Liebscher (2014) <doi:10.2478/demo-2014-0004>; Liebscher (2017) <doi:10.1515/demo-2017-0012>; Liebscher (2019, submitted).
	"""
	
	cran = "depcoeff" 

	version("0.0.1", md5="e9e129fdd1658581b2c9befc5fced9f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))

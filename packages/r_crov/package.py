# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrov(RPackage):
	"""Constrained Regression Model for an Ordinal Response and Ordinal
Predictors

	Fits a constrained regression model for an ordinal response with ordinal predictors and possibly others, Espinosa and Hennig (2019) <DOI:10.1007/s11222-018-9842-2>. The parameter estimates associated with an ordinal predictor are constrained to be monotonic. If a monotonicity direction (isotonic or antitonic) is not specified for an ordinal predictor by the user, then one of the available methods will either establish it or drop the monotonicity assumption. Two monotonicity tests are also available to test the null hypothesis of monotonicity over a set of parameters associated with an ordinal predictor.
	"""
	
	cran = "crov" 

	version("0.3.0", md5="16d8a437fd1d15e321567c6cdbc4911a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vgam@1.0.5:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))

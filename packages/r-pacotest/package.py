# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPacotest(RPackage):
	"""Testing for Partial Copulas and the Simplifying Assumption in
Vine Copulas

	Routines for two different test types, the Constant Conditional Correlation (CCC) test and the Vectorial Independence (VI) test are provided (Kurz and Spanhel (2022) <doi:10.1214/22-EJS2051>). The tests can be applied to check whether a conditional copula coincides with its partial copula. Functions to test whether a regular vine copula satisfies the so-called simplifying assumption or to test a single copula within a regular vine copula to be a (j-1)-th order partial copula are available. The CCC test comes with a decision tree approach to allow testing in high-dimensional settings.
	"""
	
	cran = "pacotest" 

	version("0.4.2", md5="508b3460d41e7ddc173aed67a8e7a047")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vinecopula@2.0.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

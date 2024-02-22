# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobnptests(RPackage):
	"""Robust Nonparametric Two-Sample Tests for Location/Scale

	Implementations of several robust nonparametric two-sample tests
    for location or scale differences. The test statistics are based on robust
    location and scale estimators, e.g. the sample median or the Hodges-Lehmann estimators
    as described in Fried & Dehling (2011) <doi:10.1007/s10260-011-0164-1>.
    The p-values can be computed via the permutation principle, the randomization principle, or by using
    the asymptotic distributions of the test statistics under the null hypothesis, which ensures
    (approximate) distribution independence of the test decision. To test for a difference in
    scale, we apply the tests for location difference to transformed observations; see Fried (2012) <doi:10.1016/j.csda.2011.02.012>.
    Random noise on a small range can be added to the original observations in order to
    hold the significance level on data from discrete distributions.
    The location tests assume homoscedasticity and the scale tests require the
    location parameters to be zero.
	"""
	
	homepage = "https://github.com/s-abbas/robnptests"
	cran = "robnptests" 

	version("1.1.0", md5="d87079fffae0dc36e0cd396314eba815")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))

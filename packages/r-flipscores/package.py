# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlipscores(RPackage):
	"""Robust Score Testing in GLMs, by Sign-Flip Contributions

	Provides robust tests for testing in GLMs, by sign-flipping score contributions. The tests are robust against overdispersion, heteroscedasticity and, in some cases, ignored nuisance variables. See Hemerik, Goeman and Finos (2020) <doi:10.1111/rssb.12369>.
	"""
	
	cran = "flipscores" 

	version("1.2.0", md5="3f9c1b7a28d14072dbb9b84a1604a808")

	depends_on("r-mass", type=("build", "run"))

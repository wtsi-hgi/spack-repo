# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrt(RPackage):
	"""Single-Case Randomization Tests

	Design single-case phase, alternation and multiple-baseline experiments, and conduct randomization tests on data gathered by means of such designs, as discussed in Bulte and Onghena (2013) <doi:10.22237/jmasm/1383280020>.
	"""
	
	cran = "SCRT" 

	version("1.3.1", md5="929c4790263d83973abf2dc8b98eacc6")

	depends_on("r@2.14.1:", type=("build", "run"))

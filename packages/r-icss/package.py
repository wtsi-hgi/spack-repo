# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcss(RPackage):
	"""ICSS Algorithm by Inclan/Tiao (1994)

	The Iterative Cumulative Sum of Squares (ICSS) algorithm by Inclan/Tiao (1994) <https://www.jstor.org/stable/2290916> detects multiple change points, i.e. structural break points, in the variance of a sequence of independent observations. For series of moderate size (i.e. 200 observations and beyond), the ICSS algorithm offers results comparable to those obtained by a Bayesian approach or by likelihood ration tests, without the heavy computational burden required by these approaches.
	"""
	
	cran = "ICSS" 

	version("1.1", md5="9c45f23be73116e8ae9bd90563e1c149")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstack", type=("build", "run"))

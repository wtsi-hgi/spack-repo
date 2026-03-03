# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReldist(RPackage):
	"""Relative Distribution Methods

	Tools for the comparison of distributions. This includes nonparametric estimation of the relative distribution PDF and CDF and numerical summaries as described in "Relative Distribution Methods in the Social Sciences" by Mark S. Handcock and Martina Morris, Springer-Verlag, 1999, Springer-Verlag, ISBN 0387987789.
	"""
	
	homepage = "http://www.stat.ucla.edu/~handcock/RelDist/"
	cran = "reldist" 

	version("1.7-2", md5="eb0792706594b5ea0e2e2ce5fa41b2f4")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-densestbayes", type=("build", "run"))

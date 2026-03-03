# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactci(RPackage):
	"""Exact P-Values and Matching Confidence Intervals for Simple
Discrete Parametric Cases

	Calculates exact tests and confidence intervals for one-sample binomial and one- or two-sample Poisson cases (see Fay (2010) <doi:10.32614/rj-2010-008>). 
	"""
	
	cran = "exactci" 

	version("1.4-4", md5="447f19a10800a1e7ac09201268e83c3a")

	depends_on("r-ssanv", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))

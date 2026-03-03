# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveltest(RPackage):
	"""Comparing Multiple Survival Functions with Crossing Hazards

	Computing the one-sided/two-sided integrated/maximally selected EL statistics for simultaneous testing, the one-sided/two-sided EL tests for pointwise testing, and an initial test that precedes one-sided testing to exclude the possibility of crossings or alternative orderings among the survival functions. 
	"""
	
	homepage = "https://github.com/news11/survELtest"
	cran = "survELtest" 

	version("2.0.1", md5="55674c61fce6fd2a84d9ad74828d1670")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

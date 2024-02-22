# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCattexact(RPackage):
	"""Computation of the p-Value for the Exact Conditional
Cochran-Armitage Trend Test

	Provides functions for computing the one-sided p-values of the Cochran-Armitage trend test
  statistic for the asymptotic and the exact conditional test. The computation of the p-value for the exact test
  is performed using an algorithm following an idea by Mehta, et al. (1992) <doi:10.2307/1390598>.
	"""
	
	cran = "CATTexact" 

	version("0.1.1", md5="14b28720dfb77ad951780c1c9d8a682c")

	depends_on("r@3.6:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartiallyoverlapping(RPackage):
	"""Partially Overlapping Samples Tests

	Tests for a comparison of two partially overlapping samples.
  A comparison of means using the partially overlapping samples t-test: 
  See Derrick, Russ, Toher and White (2017), Test 
  statistics for the comparison of means for two samples which include 
  both paired observations and independent observations, Journal of 
  Modern Applied Statistical Methods, 16(1). 
  A comparison of proportions using the partially overlapping samples z-test:
  See Derrick, Dobson-Mckittrick, Toher and White (2015), Test statistics
  for comparing two proportions with partially overlapping samples.
  Journal of Applied Quantitative Methods, 10(3).
	"""
	
	cran = "Partiallyoverlapping" 

	version("2.0", md5="f445fa96066dcbdf27888342975105cf")

	depends_on("r@3.1.3:", type=("build", "run"))

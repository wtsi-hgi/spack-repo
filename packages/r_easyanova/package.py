# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyanova(RPackage):
	"""Analysis of Variance and Other Important Complementary Analyses

	Perform analysis of variance and other important complementary
  analyses.  The functions are easy to use.  Performs analysis in various
  designs, with balanced and unbalanced data.
	"""
	
	cran = "easyanova" 

	version("10.0", md5="d257b04d684586724aa93d2a90b026a9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmBr(RPackage):
	"""Linear Model with Breakpoint

	Exact significance tests for a changepoint in linear or multiple linear regression.  
  Confidence regions with exact coverage probabilities for the changepoint.  Based on 
  Knowles, Siegmund and Zhang (1991) <doi:10.1093/biomet/78.1.15>.
	"""
	
	cran = "lm.br" 

	version("2.9.7", md5="8952107ef6d7f06b9eafb13f05d8c6e5")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

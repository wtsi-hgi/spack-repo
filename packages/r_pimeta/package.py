# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPimeta(RPackage):
	"""Prediction Intervals for Random-Effects Meta-Analysis

	An implementation of prediction intervals for random-effects meta-analysis:
  Higgins et al. (2009) <doi:10.1111/j.1467-985X.2008.00552.x>, Partlett and Riley (2017)
  <doi:10.1002/sim.7140>, and Nagashima et al. (2019) <doi:10.1177/0962280218773520>,
  <arXiv:1804.01054>.
	"""
	
	cran = "pimeta" 

	version("1.1.3", md5="a28f7f109dc025b754a14674d9605001")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

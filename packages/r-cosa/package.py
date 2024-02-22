# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosa(RPackage):
	"""Bound Constrained Optimal Sample Size Allocation

	
  Implements bound constrained optimal sample size allocation (BCOSSA) framework described in Bulus & Dong (2021) <doi:10.1080/00220973.2019.1636197> for power analysis of multilevel regression discontinuity designs (MRDDs) and multilevel randomized trials (MRTs) with continuous outcomes.
  Minimum detectable effect size (MDES) and power computations for MRDDs allow polynomial functional form specification for the score variable (with or without interaction with the treatment indicator). See Bulus (2021) <doi:10.1080/19345747.2021.1947425>. 
	"""
	
	cran = "cosa" 

	version("2.1.0", md5="1fdfecbcbc94dd788477c821eb04e215")

	depends_on("r-nloptr@1.0.4:", type=("build", "run"))
	depends_on("r-msm@1.6.7:", type=("build", "run"))

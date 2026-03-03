# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoboost(RPackage):
	"""Isotonic Boosting Classification Rules

	In classification problems a monotone relation between some
  predictors and the classes may be assumed. In this package 'isoboost' 
  we propose new boosting algorithms, based on LogitBoost, that 
  incorporate this isotonicity information, yielding more accurate 
  and easily interpretable rules.
	"""
	
	cran = "isoboost" 

	version("1.0.1", md5="b82db1056a11391218f9bfc623aa1262")

	depends_on("r-iso", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))

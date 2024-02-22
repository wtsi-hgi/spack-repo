# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYhat(RPackage):
	"""Interpreting Regression Effects

	The purpose of this package is to provide methods to interpret multiple
  linear regression and canonical correlation results including beta weights,structure coefficients, 
  validity coefficients, product measures, relative weights, all-possible-subsets regression,
  dominance analysis, commonality analysis, and adjusted effect sizes.
	"""
	
	cran = "yhat" 

	version("2.0-4", md5="60df8b757a0bea80fc50532b6b854a9d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-yacca", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))

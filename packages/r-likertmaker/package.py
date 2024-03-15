# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikertmaker(RPackage):
	"""Synthesise and Correlate Rating-Scale Data

	Synthesise rating-scale data with predefined 
  first & second moments (mean & standard deviation) and, optionally, 
  correlate multiple vectors with predefined correlation matrix. 
  Also generate synthetic rating-scale data with predefined Cronbach's Alpha.
	"""
	
	homepage = "https://github.com/WinzarH/LikertMakeR"
	cran = "LikertMakeR" 

	version("0.2.0", md5="7a385fb5d33847b266805c0ec5fcdcba")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

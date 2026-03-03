# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCate(RPackage):
	"""High Dimensional Factor Analysis and Confounder Adjusted Testing
and Estimation

	Provides several methods for factor analysis in high dimension (both n,p >> 1) and methods to adjust for possible confounders in multiple hypothesis testing.
	"""
	
	cran = "cate" 

	version("1.1.1", md5="72f13380c85b3a7417250f9d79d1b7e3")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-esabcv", type=("build", "run"))
	depends_on("r-ruv", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-leapp", type=("build", "run"))

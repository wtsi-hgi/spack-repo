# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcpen(RPackage):
	"""Penalized Variance Components Analysis

	Method to perform penalized variance component analysis.
	"""
	
	homepage = "https://cran.r-project.org/package=vcpen"
	cran = "vcpen" 

	version("1.9", md5="a1d2a9aa84f9b5e28b66ef71b8c17597")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

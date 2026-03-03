# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmem(RPackage):
	"""Multivariate Mixed Effects Model

	Analyzing data under multivariate mixed effects model using multivariate REML and multivariate Henderson3 methods. 
  See Meyer (1985) <doi:10.2307/2530651> and Wesolowska Janczarek (1984) <doi:10.1002/bimj.4710260613>.
	"""
	
	cran = "MMeM" 

	version("0.1.1", md5="7299df16de5cbcdc5e310776fad0e96e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-jointdiag", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLslx(RPackage):
	"""Semi-Confirmatory Structural Equation Modeling via Penalized
Likelihood or Least Squares

	Fits semi-confirmatory structural equation modeling (SEM) via penalized likelihood (PL) or penalized least squares (PLS). For details, please see Huang (2020) <doi:10.18637/jss.v093.i07>.
	"""
	
	homepage = "https://github.com/psyphh/lslx/wiki"
	cran = "lslx" 

	version("0.6.11", md5="605554ed6f0d909592261956425361c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLesssem(RPackage):
	"""Non-Smooth Regularization for Structural Equation Models

	Provides regularized structural equation modeling 
  (regularized SEM) with non-smooth penalty functions (e.g., lasso) building 
  on 'lavaan'. The package is heavily inspired by the 
  ['regsem'](<https://github.com/Rjacobucci/regsem>) and 
  ['lslx'](<https://github.com/psyphh/lslx>) packages.
	"""
	
	homepage = "https://github.com/jhorzek/lessSEM"
	cran = "lessSEM" 

	version("1.5.5", md5="b0555099095b623f3eac90ffeda0971d")

	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

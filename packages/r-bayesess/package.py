# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesess(RPackage):
	"""Determining Effective Sample Size

	Determines effective sample size of a parametric prior distribution
    in Bayesian models. For a web-based Shiny application related to this package, see <https://implement.shinyapps.io/bayesess/>. 
	"""
	
	cran = "BayesESS" 

	version("0.1.19", md5="5e51846c33125294df78c6d6c71620c0")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dfcrm", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

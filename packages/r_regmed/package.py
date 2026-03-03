# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegmed(RPackage):
	"""Regularized Mediation Analysis

	Mediation analysis for multiple mediators by penalized structural equation models with different types of penalties depending on whether there are multiple mediators and only one exposure and one outcome variable (using sparse group lasso) or multiple exposures, multiple mediators, and multiple outcome variables (using lasso, L1, penalties).
	"""
	
	homepage = "https://cran.r-project.org/package=regmed"
	cran = "regmed" 

	version("2.1.0", md5="ee73e1f0a954ab5123fea67214c15c50")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))

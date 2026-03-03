# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBujar(RPackage):
	"""Buckley-James Regression for Survival Data with High-Dimensional
Covariates

	Buckley-James regression for right-censoring survival data with high-dimensional covariates. Implementations for survival data include boosting with componentwise linear least squares, componentwise smoothing splines, regression trees and MARS. Other high-dimensional tools include penalized regression for survival data. See Wang and Wang (2010) <doi:10.2202/1544-6115.1550>.
	"""
	
	cran = "bujar" 

	version("0.2-11", md5="6d36de02a560bc6960607d5a920d68e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-mpath", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-bst", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

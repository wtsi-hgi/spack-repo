# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychonetrics(RPackage):
	"""Structural Equation Modeling and Confirmatory Network Analysis

	Multi-group (dynamical) structural equation models in combination with confirmatory network models from cross-sectional, time-series and panel data <doi:10.31234/osf.io/8ha93>. Allows for confirmatory testing and fit as well as exploratory model search.
	"""
	
	homepage = "http://psychonetrics.org/"
	cran = "psychonetrics" 

	version("0.11.5", md5="f67ad25b623704093f11acb01d930eac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-vca", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-isingsampler", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp@0.11.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-pbv", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))

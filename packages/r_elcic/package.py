# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElcic(RPackage):
	"""The Empirical Likelihood-Based Consistent Information Criterion

	We developed a consistent and robust information criterion to conduct model selection for semiparametric models. It is free of distribution specification and powerful to locate the true model given large sample size. This package provides several usage of ELCIC with applications in generalized linear model (GLM), generalized estimating equation (GEE) for longitudinal data, and weighted GEE (WGEE) for missing longitudinal data under the mechanism of missing at random and drop-out. Chixaing Chen, Ming Wang, Rongling Wu, Runze Li (2020) <doi:10.5705/ss.202020.0254>.  
	"""
	
	homepage = "https://github.com/chencxxy28/ELCIC"
	cran = "ELCIC" 

	version("0.2.1", md5="fbc9e15db445b7f1138d3b7c8aef730c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-poisnor", type=("build", "run"))
	depends_on("r-bindata", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-wgeesel", type=("build", "run"))

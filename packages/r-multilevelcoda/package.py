# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilevelcoda(RPackage):
	"""Estimate Bayesian Multilevel Models for Compositional Data

	Implement Bayesian Multilevel Modelling for compositional data 
             in a multilevel framework. Compute multilevel compositional data and 
             Isometric log ratio (ILR) at between and within-person levels, 
             fit Bayesian multilevel models for compositional predictors and outcomes, 
             and run post-hoc analyses such as isotemporal substitution models.
	"""
	
	homepage = "https://florale.github.io/multilevelcoda/"
	cran = "multilevelcoda" 

	version("1.2.3", md5="0c7d48b04fb2e486787767ff5fa34823")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-extraoperators", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))

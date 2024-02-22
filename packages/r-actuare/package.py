# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActuare(RPackage):
	"""Handling Hierarchically Structured Risk Factors using Random
Effects Models

	Using this package, you can fit a random effects model using either the hierarchical credibility model, a combination of the hierarchical credibility model with a generalized linear model or a Tweedie generalized linear mixed model. See Campo, B.D.C. and Antonio, K. (2023) <doi:10.1080/03461238.2022.2161413>.
	"""
	
	homepage = "https://bavodc.github.io/websiteactuaRE/"
	cran = "actuaRE" 

	version("0.1.5", md5="d3f79dcf14e8ed9fec1ee610e42f4632")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cplm", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))

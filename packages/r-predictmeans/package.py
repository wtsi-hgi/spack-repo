# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictmeans(RPackage):
	"""Predicted Means for Linear and Semiparametric Models

	Providing functions to diagnose and make inferences from various linear models, 
    such as those obtained from 'aov', 'lm', 'glm', 'gls', 'lme', 'lmer', 'glmmTMB' and 'semireg'. 
	Inferences include predicted means and standard errors, contrasts, multiple comparisons, 
	permutation tests, adjusted R-square and graphs.
	"""
	
	homepage = "https://CRAN.R-project.org/package=predictmeans"
	cran = "predictmeans" 

	version("1.1.0", md5="2629a2d736d22fd10921ed6b82559b36")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hrw", type=("build", "run"))
	depends_on("r-lmeinfo", type=("build", "run"))
	depends_on("r-lmesplines", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))

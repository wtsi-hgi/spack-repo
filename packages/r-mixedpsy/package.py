# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedpsy(RPackage):
	"""Statistical Tools for the Analysis of Psychophysical Data

	Tools for the analysis of psychophysical data in R. This package allows to estimate the Point of Subjective Equivalence (PSE) 
    and the Just Noticeable Difference (JND), either from a psychometric function or from a Generalized Linear Mixed Model (GLMM). 
    Additionally, the package allows plotting the fitted models and the response data, simulating psychometric functions of different shapes, and simulating data sets.
    For a description of the use of GLMMs applied to psychophysical data, refer to Moscatelli et al. (2012).
	"""
	
	homepage = "https://mixedpsychophysics.wordpress.com"
	cran = "MixedPsy" 

	version("1.1.0", md5="e667036f9c378e7725274e0dbbc53c40")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-brglm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

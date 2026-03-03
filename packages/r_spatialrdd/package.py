# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialrdd(RPackage):
	"""Conduct Multiple Types of Geographic Regression Discontinuity
Designs

	Spatial versions of Regression Discontinuity Designs (RDDs) are becoming increasingly popular as tools for causal inference. However, conducting state-of-the-art analyses often involves tedious and time-consuming steps. This package offers comprehensive functionalities for executing all required spatial and econometric tasks in a streamlined manner. Moreover, it equips researchers with tools for performing essential placebo and balancing checks comprehensively. The fact that researchers do not have to rely on 'APIs' of external 'GIS' software ensures replicability and raises the standard for spatial RDDs.
	"""
	
	homepage = "https://axlehner.github.io/SpatialRDD/"
	cran = "SpatialRDD" 

	version("0.1.0", md5="e60d2ec0a0da972ad9ee3f4fd31deb28")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdrobust", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))

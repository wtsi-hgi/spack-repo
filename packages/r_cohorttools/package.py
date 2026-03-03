# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohorttools(RPackage):
	"""Cohort Data Analyses

	Functions to make lifetables and to calculate hazard function estimate using Poisson regression model with splines. Includes function to draw simple flowchart of cohort study. Function boxesLx() makes boxes of transition rates between states. It utilizes 'Epi' package 'Lexis' data.
	"""
	
	cran = "cohorttools" 

	version("0.1.6", md5="0861fb7fd83aad27f94ceb3a08f16d5f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))

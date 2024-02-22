# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrtspat(RPackage):
	"""Workflow for Cluster Randomised Trials with Spillover

	Design, workflow and statistical analysis of Cluster Randomised Trials of (health) interventions where there may be spillover between the arms (see <https://thomasasmith.github.io/index.html>). 
	"""
	
	cran = "CRTspat" 

	version("1.2.0", md5="36a072807fc3726e06c15ea6843ee5b3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-oor", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-jagsui", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))

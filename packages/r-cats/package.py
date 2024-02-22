# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCats(RPackage):
	"""Cohort Platform Trial Simulation

	Cohort plAtform Trial Simulation whereby every cohort consists of two arms, 
             control and experimental treatment. Endpoints are co-primary binary endpoints and
             decisions are made using either Bayesian or frequentist decision rules. 
             Realistic trial trajectories are simulated and the operating characteristics of the 
             designs are calculated.
	"""
	
	cran = "cats" 

	version("1.0.2", md5="f367742a02af4133b53b833d91e9e7f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

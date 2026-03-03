# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REiexpand(RPackage):
	"""Utilities for Expanding Functionality of 'eiCompare'

	Augments the 'eiCompare' package's Racially Polarized Voting (RPV) 
  functionality to streamline analyses and visualizations used to support 
  voting rights and redistricting litigation. The package implements methods 
  described in Barreto, M., Collingwood, L., Garcia-Rios, S., & Oskooii, K. A. (2022). 
  "Estimating Candidate Support in Voting Rights Act Cases: Comparing Iterative 
  EI and EI-R×C Methods" <doi:10.1177/0049124119852394>.
	"""
	
	cran = "eiExpand" 

	version("1.0.5", md5="e1a671ac46517f5be72b59e7bd1de2fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

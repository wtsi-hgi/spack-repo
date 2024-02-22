# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProae(RPackage):
	"""PRO-CTCAE Scoring, Analysis, and Graphical Tools

	A collection of tools to facilitate standardized analysis 
    and graphical procedures when using the National Cancer Institute’s 
    Patient-Reported Outcomes version of the Common Terminology Criteria for 
    Adverse Events (PRO-CTCAE).
	"""
	
	cran = "ProAE" 

	version("0.2.15", md5="67134b77dd3a2821d0153c713d536a6f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggpattern", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsurvey(RPackage):
	"""Simplifying 'ggplot2' for Survey Data

	Functions for survey data including svydesign objects from the 'survey' package that call 'ggplot2' to make bar charts, histograms, boxplots, and hexplots of survey data.  
	"""
	
	cran = "ggsurvey" 

	version("1.0.0", md5="ef78a2e51dbb617ce21de4a332a77fcd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

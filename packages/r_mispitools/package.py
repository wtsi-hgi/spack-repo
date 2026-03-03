# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMispitools(RPackage):
	"""Missing Person Identification Tools

	A set of decision making tools to conduct missing person searches.  Particularly, it allows computing optimal LR threshold for declaring potential matches in DNA-based database search. More recently 'mispitools' incorporates preliminary investigation data based LRs. Statistical weight of different traces of evidence such as biological sex, age and hair color are presented. For citing mispitools please use the following references: Marsico and Caridi, 2023 <doi:10.1016/j.fsigen.2023.102891> and  Marsico, Vigeland et al. 2021 <doi:10.1016/j.fsigen.2021.102519>.
	"""
	
	homepage = "https://github.com/MarsicoFL/mispitools"
	cran = "mispitools" 

	version("1.0.0", md5="857574401b94c913f732f9b706f6990d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forrel", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dirichletreg", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))

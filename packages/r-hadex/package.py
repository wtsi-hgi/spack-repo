# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHadex(RPackage):
	"""Analysis and Visualisation of Hydrogen/Deuterium Exchange Mass
Spectrometry Data

	Functions for processing, analysis and visualization of Hydrogen Deuterium eXchange monitored by 
             Mass Spectrometry experiments (HDX-MS) (10.1093/bioinformatics/btaa587). 'HaDeX' introduces a new 
             standardized and reproducible workflow for the analysis of the HDX-MS data, including novel 
             uncertainty intervals. Additionally, it covers data exploration, quality control and generation of 
             publication-quality figures. All functionalities are also available in the in-built 'Shiny' app.
	"""
	
	cran = "HaDeX" 

	version("1.2.2", md5="7afa57f4ebb273f6895d21e7b77f96ab")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

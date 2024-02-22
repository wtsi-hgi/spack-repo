# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadshapr(RPackage):
	"""Support Technical Processes Following 'Maelstrom Research'
Standards

	Functions to support rigorous processes in data cleaning, 
     evaluation, and documentation across datasets from different studies based 
     on Maelstrom Research guidelines. The package includes the core functions 
     to evaluate and format the main inputs that define the process, diagnose 
     errors, and summarize and evaluate datasets and their associated 
     data dictionaries. The main outputs are clean datasets and associated 
     metadata, and tabular and visual summary reports. As described in 
     Maelstrom Research guidelines for rigorous retrospective data 
     harmonization (Fortier I and al. (2017) <doi:10.1093/ije/dyw075>).
	"""
	
	homepage = "https://github.com/maelstrom-research/madshapR"
	cran = "madshapR" 

	version("1.0.3", md5="7676578abc85428eb1854378871588c6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-fabr@2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScicomptools(RPackage):
	"""Tools Developed by the NCEAS Scientific Computing Support Team

	Set of tools to import, summarize, wrangle, and visualize data. 
    These functions were originally written based on the needs of the 
    various synthesis working groups that were supported by the 
    National Center for Ecological Analysis and Synthesis (NCEAS). 
    These tools are meant to be useful inside and 
    outside of the context for which they were designed. 
	"""
	
	homepage = "https://github.com/NCEAS/scicomptools"
	cran = "scicomptools" 

	version("1.0.0", md5="29fe918c7e022a688ba43732840d8cb9")

	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gitcreds", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-semnetcleaner", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tidyxl", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSendigr(RPackage):
	"""Enable Cross-Study Analysis of 'CDISC' 'SEND' Datasets

	A system enables cross study Analysis by extracting and filtering study data for 
    control animals from  'CDISC' 'SEND' Study Repository. 
    These data types are supported: Body Weights, Laboratory test results and Microscopic findings. 
    These database types are supported: 'SQLite' and 'Oracle'.
	"""
	
	homepage = "https://github.com/phuse-org/sendigR"
	cran = "sendigR" 

	version("1.0.0", md5="53cef797d238f1ab61c880e78521ccd2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-cicerone", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("python@3.9.6:", type=("build", "link", "run"))

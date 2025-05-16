# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinalfit(RPackage):
	"""Quickly Create Elegant Regression Results Tables and Plots when
Modelling

	Generate regression results tables and plots in final 
    format for publication. Explore models and export directly to PDF 
    and 'Word' using 'RMarkdown'. 
	"""
	
	homepage = "https://github.com/ewenharrison/finalfit"
	cran = "finalfit" 

	version("1.0.7", md5="70920ff6889cf6547d0edce1b120cc59")
	version("1.0.6", md5="49745639a6fc029760c7d6a71bcb68dd")

	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))

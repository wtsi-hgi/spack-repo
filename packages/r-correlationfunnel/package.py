# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrelationfunnel(RPackage):
	"""Speed Up Exploratory Data Analysis (EDA) with the Correlation
Funnel

	
    Speeds up exploratory data analysis (EDA)
    by providing a succinct workflow and interactive visualization tools for understanding
    which features have relationships to target (response). Uses binary correlation analysis
    to determine relationship. Default correlation method is the Pearson method. 
    Lian Duan, W Nick Street, Yanchi Liu, Songhua Xu, and Brook Wu (2014) <doi:10.1145/2637484>.
	"""
	
	homepage = "https://github.com/business-science/correlationfunnel"
	cran = "correlationfunnel" 

	version("0.2.0", md5="b50262a90c0091b9ec31c225ba8d653e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))

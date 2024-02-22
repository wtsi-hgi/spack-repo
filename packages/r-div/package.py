# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiv(RPackage):
	"""Report on Diversity and Inclusion in a Corporate Setting

	Facilitate the analysis of teams in a corporate setting:
    assess the diversity per grade and job, present the results,
    search for bias (in hiring and/or promoting processes).
    It also provides methods to simulate the effect of bias, random team-data, etc.
    White paper: 'Philippe J.S. De Brouwer' (2021) <http://www.de-brouwer.com/assets/div/div-white-paper.pdf>.
    Book (chapter 36): 'Philippe J.S. De Brouwer' (2020, ISBN:978-1-119-63272-6) and 'Philippe J.S. De Brouwer' (2020) <doi:10.1002/9781119632757>.
	"""
	
	homepage = "http://www.de-brouwer.com/div/"
	cran = "div" 

	version("0.3.1", md5="b510c10f377785aef189de56cd93296f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))

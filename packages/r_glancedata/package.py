# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlancedata(RPackage):
	"""Generate tables and plots to get summaries of data

	Generate data frames for all the variables with some summaries and also some plots for numerical variables.
    Several functions from the 'tidyverse' and 'GGally' packages are used.
	"""
	
	cran = "glancedata" 

	version("1.0.1", md5="755a51a18325b296146900f988765003")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))

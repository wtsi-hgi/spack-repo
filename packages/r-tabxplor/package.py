# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabxplor(RPackage):
	"""User-Friendly Tables with Color Helpers for Data Exploration

	Make it easy to deal with multiple cross-tables in data 
    exploration, by creating them, manipulating them, and adding color 
    helpers to highlight important informations (differences from totals, 
    comparisons between lines or columns, contributions to variance, margins 
    of error, etc.). All functions are pipe-friendly and render data frames 
    which can be easily manipulated. In the same time, time-taking operations 
    are done with 'data.table' to go faster with big dataframes. Tables can
    be exported to 'Excel' and in html with formats and colors.
	"""
	
	homepage = "https://github.com/BriceNocenti/tabxplor"
	cran = "tabxplor" 

	version("1.1.3", md5="0f5cf192376ffbc5542961c12abe6965")

	depends_on("r-dplyr@1.0.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-crayon@1.3:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-stringi@1.4.6:", type=("build", "run"))
	depends_on("r-pillar@1.6:", type=("build", "run"))
	depends_on("r-kableextra@1.3:", type=("build", "run"))
	depends_on("r-desctools@0.99:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

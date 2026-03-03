# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeachingapps(RPackage):
	"""Apps for Teaching Statistics, R Programming, and Shiny App
Development

	Contains apps and gadgets for teaching data analysis and 
    statistics concepts along with how to implement them in R.  Includes 
    tools to make app development easier and faster by nesting apps together.
	"""
	
	homepage = "https://github.com/Auburngrads/teachingApps"
	cran = "teachingApps" 

	version("1.0.8", md5="e516079838aac62c3aa01ada0322a58c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-pacman", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp@0.12.14:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-bh@1.58.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

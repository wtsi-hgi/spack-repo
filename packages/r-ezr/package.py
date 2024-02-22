# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzr(RPackage):
	"""Easy Use of R via Shiny App for Basic Analyses of Experimental
Data

	Runs a Shiny App in the local machine for basic
    statistical and graphical analyses. The point-and-click interface 
    of Shiny App enables obtaining the same analysis outputs (e.g., plots and
    tables) more quickly, as compared with typing the required code in R,
    especially for users without much experience or expertise with coding.
    Examples of possible analyses include tabulating descriptive
    statistics for a variable, creating histograms by experimental groups,
    and creating a scatter plot and calculating the correlation between
    two variables.
	"""
	
	homepage = "https://github.com/jinkim3/ezr"
	cran = "ezr" 

	version("0.1.5", md5="2c618ae94078b941603b9a83f10236f2")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))

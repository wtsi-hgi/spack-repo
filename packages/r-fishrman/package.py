# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishrman(RPackage):
	"""The Fisheries Scientist's Toolbox

	A bundle of analytics tools for fisheries scientists. Data on fishing effort by 'Global Fishing Watch' can be retrieved via the package's API <https://fishrman.ddnsfree.com/gfw>, as well as data on Exclusive Economic Zones by 'Marine Regions'. A 'shiny' R App is included for a 'no-code' solution for retrieval, analysis, and visualization.
	"""
	
	homepage = "https://github.com/Shyentist/fish-r-man"
	cran = "fishRman" 

	version("1.2.2", md5="bd9af58ec2d65475ee4549f49108c94a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhecodemap(RPackage):
	"""Visualization for PheCode Mapping with ICD-9 and ICD-10-CM Codes

	To build a shiny app for visualization of the hierarchy of PheCode Mapping with International Classification of Diseases (ICD). The same PheCode hierarchy is displayed in two ways: as a sunburst plot and as a tree.
	"""
	
	homepage = "https://github.com/celehs/phecodemap"
	cran = "phecodemap" 

	version("0.1.0", md5="7b190e51199f834b6641564f7c4b237d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-collapsibletree", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestanaapp(RPackage):
	"""The 'shiny' App for Test Analysis and Visualization

	This application enables exploratory factor analysis, confirmatory factor analysis, classical measurement theory analysis, unidimensional item response theory, multidimensional item response theory, and continuous item response model analysis, through the 'shiny' interactive interface. It also facilitates the visualization of the results. Users can easily download the analysis results from the interactive interface. Additionally, users can download a concise report about items and test quality on the interactive interface.
	"""
	
	homepage = "https://github.com/jiangyouxiang/TestAnaAPP"
	cran = "TestAnaAPP" 

	version("0.1.8", md5="fd6afea54a7bba2f5d4b73ba288838f3")

	depends_on("r-ggplot2@3.4.3:", type=("build", "run"))
	depends_on("r-mirt@1.40:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-estcrm@1.6:", type=("build", "run"))
	depends_on("r-tidysem@0.2.4:", type=("build", "run"))
	depends_on("r-dt@0.29:", type=("build", "run"))
	depends_on("r-golem@0.4.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.5:", type=("build", "run"))
	depends_on("r-officedown@0.3:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-brucer@2023.8.23:", type=("build", "run"))
	depends_on("r-officer@0.6.2:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.5.2:", type=("build", "run"))
	depends_on("r-rmarkdown@2.24:", type=("build", "run"))
	depends_on("r-plotrix@3.8.2:", type=("build", "run"))
	depends_on("r-cowplot@1.1.1:", type=("build", "run"))
	depends_on("r-flextable@0.9.2:", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))

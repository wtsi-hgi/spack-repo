# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19Analytics(RPackage):
	"""Load and Analyze Live Data from the COVID-19 Pandemic

	Load and analyze updated time series worldwide data of reported cases for the Novel Coronavirus Disease (COVID-19) from different sources, including the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE) data repository <https://github.com/CSSEGISandData/COVID-19>, "Our World in Data" <https://github.com/owid/> among several others. The datasets reporting the COVID-19 cases are available in two main modalities, as a time series sequences and aggregated data for the last day with greater spatial resolution. Several analysis, visualization and modelling functions are available in the package that will allow the user to compute and visualize total number of cases, total number of changes and growth rate globally or for an specific geographical location, while at the same time generating models using these trends; generate interactive visualizations and generate Susceptible-Infected-Recovered (SIR) model for the disease spread.
	"""
	
	homepage = "https://mponce0.github.io/covid19.analytics/"
	cran = "covid19.analytics" 

	version("2.1.3.3", md5="78154dc8f609c1f79b6315930716d657")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-collapsibletree", type=("build", "run"))

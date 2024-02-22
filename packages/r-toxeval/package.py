# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToxeval(RPackage):
	"""Exploring Biological Relevance of Environmental Chemistry
Observations

	Data analysis package for estimating potential biological effects from chemical concentrations in environmental samples. Included are a set of functions to analyze, visualize, and organize measured concentration data as it relates to user-selected chemical-biological interaction benchmark data such as water quality criteria. The intent of these analyses is to develop a better understanding of the potential biological relevance of environmental chemistry data. Results can be used to prioritize which chemicals at which sites may be of greatest concern. These methods are meant to be used as a screening technique to predict potential for biological influence from chemicals that ultimately need to be validated with direct biological assays. A description of the analysis can be found in Blackwell (2017) <doi:10.1021/acs.est.7b01613>.
	"""
	
	cran = "toxEval" 

	version("1.3.2", md5="123ce108a437dda5cb53efaac00cbf07")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dt@0.1.24:", type=("build", "run"))
	depends_on("r-leaflet@1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))

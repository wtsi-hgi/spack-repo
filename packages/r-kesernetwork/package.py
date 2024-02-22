# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKesernetwork(RPackage):
	"""Visualization of the KESER Network

	A shiny app to visualize the knowledge networks for the code concepts. Using co-occurrence matrices of EHR codes from Veterans Affairs (VA) and Massachusetts General Brigham (MGB), the knowledge extraction via sparse embedding regression (KESER) algorithm was used to construct knowledge networks for the code concepts. Background and details about the method can be found at Chuan et al. (2021) <doi:10.1038/s41746-021-00519-z>.
	"""
	
	homepage = "https://github.com/celehs/kesernetwork"
	cran = "kesernetwork" 

	version("0.1.0", md5="65cdf54bb02a822442408079fc085204")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RT2qv(RPackage):
	"""Control Qualitative Variables

	Covers k-table control analysis using multivariate control charts for qualitative variables using fundamentals of multiple correspondence analysis and multiple factor analysis. The graphs can be shown in a flat or interactive way, in the same way all the outputs can be shown in an interactive shiny panel.
	"""
	
	cran = "T2Qv" 

	version("0.2.0", md5="862c1de2683504014c384592eef9b0c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ca", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tables", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-htmltools@0.5.1.1:", type=("build", "run"))

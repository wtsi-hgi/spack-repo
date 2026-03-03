# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcweights(RPackage):
	"""Perform Weighted Linear Regression for Calibration Curve

	Automated assessment and selection of weighting factors for accurate quantification using linear calibration curve. 
 In addition, a 'shiny' App is provided, allowing users to analyze their data using an interactive graphical user interface, without any programming requirements.
	"""
	
	cran = "CCWeights" 

	version("0.1.6", md5="3d452a964d33347e7c13e7ecd98896da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-bs4dash", type=("build", "run"))
	depends_on("r-fresh", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))

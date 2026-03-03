# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisae(RPackage):
	"""Visualization of Adverse Events

	Implementation of 'shiny' app to visualize adverse events based on the Common Terminology Criteria for Adverse Events (CTCAE) using stacked correspondence analysis as described in Diniz et. al (2021)<doi:10.1186/s12874-021-01368-w>.
	"""
	
	cran = "visae" 

	version("0.2.0", md5="d49a7e3383d5da69f5b90a31c335ba88")

	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
	depends_on("r-ca@0.71:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.8.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))

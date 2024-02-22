# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMipplot(RPackage):
	"""An Open-Source Tool for Visualization of Climate Mitigation
Scenarios

	Generic functions to produce area/bar/box/line plots of data following IAMC (Integrated Assessment Modeling Consortium) submission format.
	"""
	
	cran = "mipplot" 

	version("0.3.1", md5="24cdedae6fd228e120bc4d7fc10f3d4c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny-i18n@0.2:", type=("build", "run"))
	depends_on("r-showtextdb", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

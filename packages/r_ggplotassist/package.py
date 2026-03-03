# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplotassist(RPackage):
	"""'RStudio' Addin for Teaching and Learning 'ggplot2'

	An 'RStudio' addin for teaching and learning making plot using the 'ggplot2' package.
    You can learn each steps of making plot by clicking your mouse without coding.
    You can get resultant code for the plot.
	"""
	
	homepage = "https://github.com/cardiomoon/ggplotAssist"
	cran = "ggplotAssist" 

	version("0.1.3", md5="e1d16e3272ab114c5bc86057bf78c670")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-gcookbook", type=("build", "run"))
	depends_on("r-moonbook", type=("build", "run"))
	depends_on("r-editdata", type=("build", "run"))

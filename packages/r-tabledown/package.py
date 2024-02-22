# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabledown(RPackage):
	"""Create Publication Quality Tables and Plots

	Create publication quality plots and tables for Item Response Theory and Classical Test theory based item analysis, exploratory and confirmatory factor analysis.
	"""
	
	homepage = "https://github.com/masiraji/tabledown"
	cran = "tabledown" 

	version("0.0.3", md5="1dab900959868b1758e775c7a7b2d890")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mote", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

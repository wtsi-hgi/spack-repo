# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToxsummary(RPackage):
	"""Visualize and Summarize Repeat-Dose Toxicology Study Results

	A 'shiny' app that generates plots and summary tables from repeat-dose
        toxicology study results to facilitate holistic evaluation of the drug safety of 
        active pharmaceutical ingredients (API) prior to initiation of clinical trials.
	"""
	
	homepage = "https://github.com/phuse-org/toxSummary"
	cran = "toxSummary" 

	version("1.0.0", md5="7cfc3d484d97ac9a1e0d754f9586e0cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cicerone", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydisconnect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

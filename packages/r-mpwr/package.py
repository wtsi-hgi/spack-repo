# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpwr(RPackage):
	"""Standardized Comparison of Workflows in Mass Spectrometry-Based
Bottom-Up Proteomics

	Useful functions to analyze proteomic workflows including
    number of identifications, data completeness, missed cleavages,
    quantitative and retention time precision etc. Various software
    outputs are supported such as 'ProteomeDiscoverer', 'Spectronaut',
    'DIA-NN' and 'MaxQuant'.
	"""
	
	cran = "mpwR" 

	version("0.1.5", md5="9b969f33a261a31406f0f9a682f05ff0")

	depends_on("r-comprehenr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flowtracer", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtti(RPackage):
	"""Bottom-Up Proteomics and LiP-MS Quality Control and Data
Analysis Tools

	Useful functions and workflows for proteomics quality control and data analysis of both limited proteolysis-coupled mass spectrometry (LiP-MS) (Feng et. al. (2014) <doi:10.1038/nbt.2999>) and regular bottom-up proteomics experiments. Data generated with search tools such as 'Spectronaut', 'MaxQuant' and 'Proteome Discover' can be easily used due to flexibility of functions.
	"""
	
	homepage = "https://github.com/jpquast/protti"
	cran = "protti" 

	version("0.8.0", md5="646708881eab4550eb58d1d8a035a644")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))

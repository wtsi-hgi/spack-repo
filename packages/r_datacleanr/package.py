# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatacleanr(RPackage):
	"""Interactive and Reproducible Data Cleaning

	Flexible and efficient cleaning of data with interactivity.
  'datacleanr' facilitates best practices in data analyses and reproducibility with built-in features and by translating interactive/manual operations to code. 
  The package is designed for interoperability, and so seamlessly fits into reproducible analyses pipelines in 'R'.
	"""
	
	homepage = "https://github.com/the-Hull/datacleanr"
	cran = "datacleanr" 

	version("1.0.3", md5="4761e4579324f936d3d843e290569988")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-htmltools@0.5:", type=("build", "run"))
	depends_on("r-summarytools@0.9.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.9:", type=("build", "run"))
	depends_on("r-dt@0.16:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-formatr@1.7:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-clipr@0.7.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9.2:", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.4:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-shinyfiles@0.8:", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))

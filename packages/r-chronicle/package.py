# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChronicle(RPackage):
	"""Grammar for Creating R Markdown Reports

	A system for creating R Markdown reports with a sequential syntax.
	"""
	
	cran = "chronicle" 

	version("0.3", md5="c2902897e43b1aaedd698175c90a95d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rmdformats", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-skimr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))

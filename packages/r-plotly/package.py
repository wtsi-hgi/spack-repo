# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotly(RPackage):
	"""Create Interactive Web Graphics via 'plotly.js'.

	Create interactive web graphics from 'ggplot2' graphs and/or a custom
	interface to the (MIT-licensed) JavaScript library 'plotly.js' inspired by
	the grammar of graphics."""

	cran = "plotly"

	version("4.10.4", md5="2b5620465fc14e4b294be3a18ffc2115")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.2.9001:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lazyeval@0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))

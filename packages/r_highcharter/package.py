# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighcharter(RPackage):
	"""A Wrapper for the 'Highcharts' Library

	A wrapper for the 'Highcharts' library including
    shortcut functions to plot R objects. 'Highcharts'
    <https://www.highcharts.com/> is a charting library offering
    numerous chart types with a simple configuration syntax.
	"""
	
	homepage = "https://jkunst.com/highcharter/"
	cran = "highcharter" 

	version("0.9.4", md5="ee6228cead5037927cddeb28ee431a7d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tibble@1.1:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rlang@0.1.1:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))

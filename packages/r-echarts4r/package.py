# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcharts4r(RPackage):
	"""Create Interactive Graphs with 'Echarts JavaScript' Version 5

	Easily create interactive charts by leveraging the 'Echarts Javascript' library which includes
    36 chart types, themes, 'Shiny' proxies and animations.
	"""
	
	homepage = "https://echarts4r.john-coene.com/"
	cran = "echarts4r" 

	version("0.4.5", md5="65b966e8698383740a3112f5cac81424")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMyclim(RPackage):
	"""Microclimatic Data Processing

	Handling the microclimatic data in R. The 'myClim' workflow begins
    at the reading data primary from microclimatic dataloggers,
    but can be also reading of meteorological station data from files.
    Cleaning time step, time zone settings and metadata collecting is the next step of the work flow.
    With 'myClim' tools one can crop, join, downscale, and convert microclimatic data formats, sort them into localities,
    request descriptive characteristics and compute microclimatic variables.
    Handy plotting functions are provided with smart defaults.
	"""
	
	homepage = "http://labgis.ibot.cas.cz/myclim/index.html"
	cran = "myClim" 

	version("1.1.0", md5="42e0e9550109689f4e8aa8330dd759e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))

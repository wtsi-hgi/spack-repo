# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHockeystick(RPackage):
	"""Download and Visualize Essential Climate Change Data

	Provides easy access to essential climate change datasets to non-climate experts. Users can download the latest raw data from authoritative sources and view it via pre-defined 'ggplot2' charts. Datasets include atmospheric CO2, methane, emissions, instrumental and proxy temperature records, sea levels, Arctic/Antarctic sea-ice, Hurricanes, and Paleoclimate data. Sources include: NOAA Mauna Loa Laboratory <https://gml.noaa.gov/ccgg/trends/data.html>, Global Carbon Project <https://www.globalcarbonproject.org/carbonbudget/>, NASA GISTEMP <https://data.giss.nasa.gov/gistemp/>, National Snow and Sea Ice Data Center <https://nsidc.org/home>, CSIRO <https://research.csiro.au/slrwavescoast/sea-level/measurements-and-data/sea-level-data/>, NOAA Laboratory for Satellite Altimetry <https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/> and HURDAT Atlantic Hurricane Database <https://www.aoml.noaa.gov/hrd/hurdat/Data_Storm.html>, Vostok Paleo carbon dioxide and temperature data: <doi:10.3334/CDIAC/ATG.009>.
	"""
	
	homepage = "https://cortinah.github.io/hockeystick/"
	cran = "hockeystick" 

	version("0.8.4", md5="8369b566dc86a5538fec019f2864c83d")
	version("0.8.3", md5="071dcfc21fd2d79227cf19dad1dee8c9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-treemapify", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))

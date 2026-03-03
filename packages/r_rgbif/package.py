# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgbif(RPackage):
	"""Interface to the Global Biodiversity Information Facility API

	A programmatic interface to the Web Service methods
    provided by the Global Biodiversity Information Facility (GBIF;
    <https://www.gbif.org/developer/summary>). GBIF is a database
    of species occurrence records from sources all over the globe.
    rgbif includes functions for searching for taxonomic names,
    retrieving information on data providers, getting species occurrence
    records, getting counts of occurrence records, and using the GBIF
    tile map service to make rasters summarizing huge amounts of data.
	"""
	
	homepage = "https://github.com/ropensci/rgbif"
	cran = "rgbif" 

	version("3.7.9", md5="0308589c5fc135d1df414808d19ba1a7")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-crul@0.7.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-oai@0.2.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcccite(RPackage):
	"""Querying and Managing Large Biodiversity Occurrence Datasets

	Facilitates the gathering of biodiversity occurrence data 
  from disparate sources. Metadata is managed throughout the process to facilitate 
  reporting and enhanced ability to repeat analyses.
	"""
	
	homepage = "https://docs.ropensci.org/occCite/"
	cran = "occCite" 

	version("0.5.6", md5="dcbb13b6bec7536c154aa0e4286b8d28")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bib2df", type=("build", "run"))
	depends_on("r-bien", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rgbif@3.1:", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-waffle", type=("build", "run"))

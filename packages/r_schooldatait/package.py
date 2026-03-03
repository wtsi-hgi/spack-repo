# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchooldatait(RPackage):
	"""Retrieve, Harmonise and Map Open Data Regarding the Italian
School System

	Compiles and displays the available data sets regarding the Italian school system, with a focus on the infrastructural aspects.
    Input datasets are downloaded from the web, with the aim of updating everything to real time.  
    The functions are divided in four main modules, namely 
    'Get', to scrape raw data from the web
    'Util', various utilities needed to process raw data
    'Group', to aggregate data at the municipality or province level
    'Map', to visualize the output datasets.
	"""
	
	cran = "SchoolDataIT" 

	version("0.1.1", md5="183fdd6003dc78266839d9da1249d1bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-leafpop", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))

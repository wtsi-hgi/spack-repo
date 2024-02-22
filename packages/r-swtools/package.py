# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwtools(RPackage):
	"""Helper Tools for Australian Hydrologists

	Functions to speed up work flow for hydrological analysis. 
    Focused on Australian climate data (SILO climate data), hydrological models (eWater Source) and in particular South Australia (<https://water.data.sa.gov.au> hydrological data).
	"""
	
	homepage = "https://github.com/matt-s-gibbs/SWTools"
	cran = "SWTools" 

	version("1.0.1", md5="c589b1748f9700a3238350322f082d2f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-hydrotsm", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))

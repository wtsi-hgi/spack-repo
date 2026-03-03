# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwtss(RPackage):
	"""Client for Web Time-Series Service

	Allows remote access to satellite image time 
    series provided by the web time series service (WTSS) available 
    at servers such as <https://brazildatacube.dpi.inpe.br/wtss/>. 
    The functions include listing the data sets available in WTSS servers, 
    describing the contents of a data set, and retrieving a time series 
    based on spatial location and temporal filters.
	"""
	
	homepage = "https://github.com/e-sensing/Rwtss/"
	cran = "Rwtss" 

	version("0.9.2", md5="2eeceff81373d97fc7676daa2db2f7b3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))

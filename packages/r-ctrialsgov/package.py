# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtrialsgov(RPackage):
	"""Query Data from U.S. National Library of Medicine's Clinical
Trials Database

	Tools to create and query database from the U.S. National Library
  of Medicine's Clinical Trials database <https://clinicaltrials.gov/>. Functions
  provide access a variety of techniques for searching the data using range
  queries, categorical filtering, and by searching for full-text keywords. 
  Minimal graphical tools are also provided for interactively exploring the
  constructed data.
	"""
	
	cran = "ctrialsgov" 

	version("0.2.5", md5="fcf4b4adb2106c307bf7671374e33f04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))

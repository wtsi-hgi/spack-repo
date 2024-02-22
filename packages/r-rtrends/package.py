# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrends(RPackage):
	"""Analyze Download Logs from the CRAN RStudio Mirror

	Analyze download logs from the CRAN RStudio mirror 
            (<http://cran.rstudio.com/>). 
            This CRAN mirror is the default one used in RStudio.
            The available data is the result of parsed and anonymised raw log data from
            that CRAN mirror.
	"""
	
	cran = "rtrends" 

	version("0.1.0", md5="9a0dec6b11c83e3c22e3efc6c0f2355f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

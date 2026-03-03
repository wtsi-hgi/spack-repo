# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatcanr(RPackage):
	"""Client for Statistics Canada's Open Economic Data

	An easy connection with R to Statistics Canada's Web Data Service. Open economic data (formerly known as CANSIM tables, now identified by Product IDs (PID)) are accessible as a data frame, directly in the user's R environment.
    Warin, Le Duc (2019) <doi:10.6084/m9.figshare.10544735>.
	"""
	
	homepage = "https://github.com/warint/statcanR/"
	cran = "statcanR" 

	version("0.2.6", md5="4e34538fe92009e37681d20d3b5b3948")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

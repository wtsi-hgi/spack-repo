# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPuzzle(RPackage):
	"""Assembling Data Sets for Non-Linear Mixed Effects Modeling

	To Simplify the time consuming and error prone task of assembling complex data sets for non-linear mixed effects modeling. Users are able to select from different absorption processes such as zero and first order, or a combination of both. Furthermore, data sets containing data from several entities, responses, and covariates can be simultaneously assembled. 
	"""
	
	homepage = "https://github.com/syneoshealth/puzzle"
	cran = "puzzle" 

	version("0.0.1", md5="610dcc6f7a81a34e5e820d3829517a64")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))

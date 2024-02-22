# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecutrialr(RPackage):
	"""Handling of Data from the Clinical Data Management System
'secuTrial'

	Seamless and standardized interaction with data
    exported from the clinical data management system (CDMS)
    'secuTrial'<https://www.secutrial.com>.
    The primary data export the package works with is a standard non-rectangular export.
	"""
	
	homepage = "https://github.com/SwissClinicalTrialOrganisation/secuTrialR"
	cran = "secuTrialR" 

	version("1.1.1", md5="7000943561af381dc9cae19ac5f5496d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-haven@2.2:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))

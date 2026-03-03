# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROralopioids(RPackage):
	"""Retrieving Oral Opioid Information

	Provides details such as Morphine Equivalent Dose (MED), 
    brand name and opioid content which are calculated of all oral opioids 
    authorized for sale by Health Canada and the FDA based on their Drug Identification Number (DIN) or National Drug Code (NDC). 
    MEDs are calculated based on recommendations by Canadian Institute for Health Information (CIHI) and Von Korff et al (2008)
    and information obtained from Health Canada's Drug Product Database's monthly data dump or FDA Daily database for Canadian and US databases respectively. 
    Please note in no way should output from this package be a substitute for medical advise.  
    All medications should only be consumed on prescription from a licensed healthcare provider.
	"""
	
	homepage = "https://github.com/ankonahouston/OralOpioids"
	cran = "OralOpioids" 

	version("2.0.3", md5="fc3764d983766b4ee9466ef2e651f1d2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

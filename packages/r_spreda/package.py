# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpreda(RPackage):
	"""Statistical Package for Reliability Data Analysis

	The Statistical Package for REliability Data Analysis (SPREDA) implements recently-developed statistical methods for the analysis of reliability data. Modern technological developments, such as sensors and smart chips, allow us to dynamically track product/system usage as well as other environmental variables, such as temperature and humidity. We refer to these variables as dynamic covariates. The package contains functions for the analysis of time-to-event data with dynamic covariates and degradation data with dynamic covariates. The package also contains functions that can be used for analyzing time-to-event data with right censoring, and with left truncation and right censoring. Financial support from NSF and DuPont are acknowledged.  
	"""
	
	cran = "SPREDA" 

	version("1.1", md5="1c2fcb0a20dde2de31ad96862002e74b")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))

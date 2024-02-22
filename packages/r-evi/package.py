# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvi(RPackage):
	"""Epidemic Volatility Index as an Early-Warning Tool

	
    This is an R package implementing the epidemic volatility index (EVI), as 
    discussed by Kostoulas et. al. (2021) and variations by Pateras et. al. (2023). EVI is a new, conceptually simple, early warning tool for oncoming epidemic waves. 
    EVI is based on the volatility of newly reported cases per unit of time,
    ideally per day, and issues an early warning when the volatility change rate exceeds a threshold.
	"""
	
	homepage = "https://www.nature.com/articles/s41598-021-02622-3"
	cran = "EVI" 

	version("0.2.0-0", md5="4cb95816dc33fa80e77d2116470b5c8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))

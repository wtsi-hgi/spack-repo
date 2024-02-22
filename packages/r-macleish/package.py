# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacleish(RPackage):
	"""Retrieve Data from MacLeish Field Station

	Download data from the Ada and Archibald MacLeish Field 
    Station in Whately, MA. The Ada 
    and Archibald MacLeish Field Station is a 260-acre patchwork of 
    forest and farmland located in West Whately, MA that provides opportunities 
    for faculty and students to pursue environmental research, outdoor 
    education, and low-impact recreation 
    (see <https://www.smith.edu/about-smith/sustainable-smith/macleish> for more information). 
    This package contains 
    weather data over several years, and spatial data on various man-made and 
    natural structures.
	"""
	
	homepage = "https://github.com/beanumber/macleish"
	cran = "macleish" 

	version("0.3.9", md5="ccae081eb701a3b9eb134a5d514bd40e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-etl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-phenocamr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))

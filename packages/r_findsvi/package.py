# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindsvi(RPackage):
	"""Calculate Social Vulnerability Index for Communities

	Developed by CDC/ATSDR (Centers for Disease Control and Prevention/
    Agency for Toxic Substances and Disease Registry), 
    Social Vulnerability Index (SVI) serves as a tool to assess the resilience 
    of communities by taking into account socioeconomic and demographic factors. 
    Provided with year(s), region(s) and a geographic level of interest, 
    'findSVI' retrieves required variables from US census data and calculates SVI 
    for communities in the specified area based on CDC/ATSDR SVI documentation. 
    Reference for the calculation methods: Flanagan BE, Gregory EW, Hallisey EJ, 
    Heitgerd JL, Lewis B (2011) <doi:10.2202/1547-7355.1792>.
	"""
	
	homepage = "https://github.com/heli-xu/findSVI"
	cran = "findSVI" 

	version("0.1.2", md5="b64206d6377285800c80e0cdc3cee211")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidycensus", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

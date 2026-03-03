# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnmarg(RPackage):
	"""Import Public Health Ontario's Ontario Marginalization Index

	The Ontario Marginalization Index is a socioeconomic model that is built on Statistics Canada census data.
    The model consists of four dimensions: In 2021, these dimensions were updated to "Material Resources" (previously called "Material Deprivation"), "Households and Dwellings" (previously called "Residential Instability"), "Age and Labour Force" (previously called "Dependency"), and "Racialized and Newcomer Populations" (previously called "Ethnic Concentration").
    This update reflects a movement away from deficit-based language. 2021 data will load with these new dimension names, wheras 2011 and 2016 data will load with the historical dimension names.
    Each of these dimensions are imported for a variety of geographic levels (DA, CD, etc.) for the 2021, 2011 and 2016 administrations of the census.
    These data sets contribute to community analysis of equity with respect to Ontario's Anti-Racism Act.
    The Ontario Marginalization Index data is retrieved from the Public Health Ontario website: <https://www.publichealthontario.ca/en/data-and-analysis/health-equity/ontario-marginalization-index>.
    The shapefile data is retrieved from the Statistics Canada website: <https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-eng.cfm>.
	"""
	
	cran = "onmaRg" 

	version("1.0.3", md5="f6ea0f55ec33972bc93688b888943362")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

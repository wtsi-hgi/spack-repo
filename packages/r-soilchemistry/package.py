# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilchemistry(RPackage):
	"""Computation of Properties Related to Soil Chemical Environment
and Nutrient Availability

	Facilitates basic and equation-based analyses of some important soil properties related to soil chemical environment and nutrient availability to plants. Freundlich H (1907). <doi:10.1515/zpch-1907-5723>. Datta SP, Bhadoria PBS (1999). <doi:10.1002%2F%28SICI%291522-2624%28199903%29162%3A2%3C183%3A%3AAID-JPLN183%3E3.0.CO%3B2-A>."Boron adsorption and desorption in some acid soils of West Bengal, India". Langmuir I (1918). <doi:10.1021/ja02242a004> "The adsorption of gases on plane surfaces of glass, mica, and platinum". Khasawneh FE (1971). <doi:10.2136/sssaj1971.03615995003500030029x> "Solution ion activity and plant growth".
	"""
	
	cran = "soilchemistry" 

	version("0.1.0", md5="aa0869a72e72fde40a7804c45b89fa3d")


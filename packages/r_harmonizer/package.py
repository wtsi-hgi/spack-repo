# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmonizer(RPackage):
	"""Harmonizing CN8 and PC8 Product Codes

	Several functions are provided to harmonize CN8 (Combined Nomenclature 
	8 digits) and PC8 (Production Communautaire 8 digits) product codes over 
	time and the classification systems HS6 and BEC. Harmonization of CN8 
	codes are possible by default from 1995 to 2022 and of PC8 from 2001 to 
	2021, respectively. 
	"""
	
	cran = "harmonizer" 

	version("0.3.2", md5="de4cbcadd7d3e070f0e49a60fb600e0b")

	depends_on("r@3.5:", type=("build", "run"))

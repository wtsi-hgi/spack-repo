# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhanesa(RPackage):
	"""NHANES Data Retrieval

	Utility to retrieve data from the National Health and Nutrition 
	Examination Survey (NHANES) website <https://www.cdc.gov/nchs/nhanes/index.htm>.
	"""
	
	homepage = "https://cran.r-project.org/package=nhanesA"
	cran = "nhanesA" 

	version("1.0", md5="4cdd96d0554f0f6d1b178c6156b59b1d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

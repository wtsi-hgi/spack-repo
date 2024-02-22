# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcdcr(RPackage):
	"""Agro-Climatic Data by County

	The functions are designed to calculate the most widely-used county-level variables in 
  agricultural production or agricultural-climatic and weather analyses. To operate some functions 
  in this package needs download of the bulk PRISM raster. See the examples, testing versions and 
  more details from: <https://github.com/ysd2004/acdcR>.
	"""
	
	homepage = "https://github.com/ysd2004/acdcR"
	cran = "acdcR" 

	version("1.0.0", md5="5bd9e3560e891df7d00817058945a9dd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

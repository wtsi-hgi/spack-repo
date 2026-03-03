# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarms(RPackage):
	"""Access Data from the USDA ARMS Data API

	Interface to easily access data via the United States Department of Agriculture (USDA)'s Agricultural Resource Management Survey (ARMS) 
  Data API <https://www.ers.usda.gov/developer/data-apis/arms-data-api/>. The downloaded data can be saved for later off-line use. 
  Also provide relevant information and metadata for each of the input variables needed for sending the data inquery.   
	"""
	
	cran = "rarms" 

	version("1.0.0", md5="c5d4f7bbaba4b9d0016cbbfe9dc3e377")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))

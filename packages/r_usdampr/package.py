# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsdampr(RPackage):
	"""Request USDA MPR Historical Data via the 'LMR' API

	Interface to easily access data via the United States Department of Agriculture (USDA)'s Livestock Mandatory Reporting ('LMR')
  Data API at <https://mpr.datamart.ams.usda.gov/>. The downloaded data can be saved for later off-line use. 
  Also provide relevant information and metadata for each of the input variables needed for sending the data inquiry.   
	"""
	
	homepage = "https://github.com/cbw1243/usdampr"
	cran = "usdampr" 

	version("1.0.1", md5="7228c9ce89d10d7213e3edb779382689")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))

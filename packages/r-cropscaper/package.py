# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCropscaper(RPackage):
	"""Access Cropland Data Layer Data via the 'CropScape' Web Service

	Interface to easily access Cropland Data Layer (CDL) data for any area of interest via the 'CropScape' <https://nassgeodata.gmu.edu/CropScape/> web service.  
	"""
	
	cran = "CropScapeR" 

	version("1.1.5", md5="639254f2b9745bc8721d321e3de5a1a8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-raster@3:", type=("build", "run"))
	depends_on("r-sf@0.8:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-rjsonio@1.3:", type=("build", "run"))

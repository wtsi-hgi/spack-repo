# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbr(RPackage):
	"""Find a Cold One Near You

	In short, this package is a locator for cool, refreshing beverages. 
  It will find and return the nearest location where you can get a cold one.
	"""
	
	cran = "pbr" 

	version("0.0.2", md5="46b2d03928aa44a5eda11a8a3d46b74e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-leaflet@2.1.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5.2:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValuemap(RPackage):
	"""Making Choropleth Map

	
    You can easily visualize your 'sf' polygons or data.frame with h3 address.
    While 'leaflet' package is too raw for data analysis, 
    this package can save data analysts' efforts & time with pre-set visualize options.
	"""
	
	homepage = "https://github.com/Curycu/valuemap"
	cran = "valuemap" 

	version("2.0.4", md5="6ae04e2a94d9ddd666c9920957ced255")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf@0.9.0:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-htmltools@0.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-devtools@2.2:", type=("build", "run"))
	depends_on("r-h3jsr@1.3:", type=("build", "run"))

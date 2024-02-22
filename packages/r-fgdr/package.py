# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgdr(RPackage):
	"""Utilities for Fundamental Geo-Spatial Data

	Read and Parse for Fundamental Geo-Spatial Data (FGD) which downloads XML file 
    from providing site (<https://fgd.gsi.go.jp/download/menu.php>). The JPGIS format file 
    provided by FGD so that it can be handled as an R spatial object such as 'sf' and 
    'raster', 'terra' or 'stars'.
    Supports the FGD version 4.1, and accepts fundamental items and digital elevation models.
	"""
	
	homepage = "https://github.com/uribo/fgdr"
	cran = "fgdr" 

	version("1.1.1", md5="93cbf3b37cbd58596d82732e955ef720")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-jpmesh@1.1.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-raster@2.6.7:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.2.2:", type=("build", "run"))
	depends_on("r-sf@0.6.3:", type=("build", "run"))
	depends_on("r-stars@0.3.1:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-terra@0.8.2:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-units@0.6.6:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))

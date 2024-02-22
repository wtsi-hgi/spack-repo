# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGiscor(RPackage):
	"""Download Map Data from GISCO API - Eurostat

	Tools to download data from the GISCO (Geographic Information
    System of the Commission) Eurostat database
    <https://ec.europa.eu/eurostat/web/gisco>. Global and European map
    data available.  This package is in no way officially related to or
    endorsed by Eurostat.
	"""
	
	homepage = "https://ropengov.github.io/giscoR/"
	cran = "giscoR" 

	version("0.4.0", md5="5c86e94c7a85365f4d0d56a1ac6c3089")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-countrycode@1.2:", type=("build", "run"))
	depends_on("r-geojsonsf@2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rappdirs@0.3:", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))

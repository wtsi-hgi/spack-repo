# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsmsearch(RPackage):
	"""DSM and LiDAR downloader

	A collection of functions to search and donwload 
    DSM (Digital Surface Model) and LiDAR (Light Detection and Ranging) data via APIs, 
    including 'OpenTopography' <https://portal.opentopography.org/apidocs/> and 
    'TNMAccess' <https://apps.nationalmap.gov/tnmaccess/#/>.
	"""
	
	cran = "dsmSearch" 

	version("1.0.0", md5="84f1ef5236900d6f364373737209ee56")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-lidr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))

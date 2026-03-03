# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopernicusdem(RPackage):
	"""Copernicus Digital Elevation Models

	Copernicus Digital Elevation Model datasets (DEM) of 90 and 30 meters resolution using the 'awscli' command line tool. The Copernicus (DEM) is included in the Registry of Open Data on 'AWS (Amazon Web Services)' and represents the surface of the Earth including buildings, infrastructure and vegetation.
	"""
	
	homepage = "https://github.com/mlampros/CopernicusDEM"
	cran = "CopernicusDEM" 

	version("1.0.3", md5="244af876be319cb6990f62dec5d21c6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("awscli", type=("build", "link", "run"))

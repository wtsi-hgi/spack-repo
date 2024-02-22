# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRczechia(RPackage):
	"""Spatial Objects of the Czech Republic

	Administrative regions and other spatial objects of the Czech Republic.
	"""
	
	homepage = "https://rczechia.jla-data.net"
	cran = "RCzechia" 

	version("1.12.0", md5="4cc6edbccaa2b3f84e51fda91cb30a94")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("gdal@2.2.3:", type=("build", "link", "run"))
	depends_on("geos@3.6.2:", type=("build", "link", "run"))
	depends_on("proj@4.9.3:", type=("build", "link", "run"))

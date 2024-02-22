# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaturalearthdata(RPackage):
	"""World Vector Map Data from Natural Earth Used in 'rnaturalearth'

	Vector map data from <https://www.naturalearthdata.com/>. Access functions are provided in the accompanying package 'rnaturalearth'.
	"""
	
	homepage = "https://docs.ropensci.org/rnaturalearthdata/"
	cran = "rnaturalearthdata" 

	version("1.0.0", md5="e2114ca233393de2bd0ae28c168752e8")

	depends_on("r@3.1.1:", type=("build", "run"))

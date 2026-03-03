# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapsperu(RPackage):
	"""Maps of Peru

	Information of the centroids and geographical limits of the regions, departments, provinces and districts of Peru.
	"""
	
	homepage = "https://github.com/musajajorge/mapsPERU"
	cran = "mapsPERU" 

	version("2.0.0", md5="93d97d6585a1045a72bcdfbeed3ca424")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

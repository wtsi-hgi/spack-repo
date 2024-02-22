# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimap(RPackage):
	"""Create Tile Grid Maps

	Create tile grid maps, which are like choropleth maps except each
  region is represented with equal visual space.
	"""
	
	homepage = "http://github.com/seankross/minimap"
	cran = "minimap" 

	version("0.1.0", md5="64a2563055812528ca98ce4167461116")

	depends_on("r@3.1:", type=("build", "run"))

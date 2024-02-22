# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapdata(RPackage):
	"""Extra Map Databases

	Supplement to maps package, providing some larger and/or
	higher-resolution databases. NOTE: this is a legacy package. The world map is out-dated.
	"""
	
	cran = "mapdata" 

	version("2.3.1", md5="a2bad641f852f9c2da756209d87c011a")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-maps@2.0.7:", type=("build", "run"))

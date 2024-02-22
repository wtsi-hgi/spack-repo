# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleangeo(RPackage):
	"""Cleaning Geometries from Spatial Objects

	
  Provides a set of utility tools to inspect spatial objects, facilitate
  handling and reporting of topology errors and geometry validity issue with sp objects.
  Finally, it provides a geometry cleaner that will fix all geometry problems,
  and eliminate (at least reduce) the likelihood of having issues when doing
  spatial data processing.
	"""
	
	homepage = "https://github.com/eblondel/cleangeo"
	cran = "cleangeo" 

	version("0.3-1", md5="25927ea605f43f7ad142d1fa063d2f4f")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))

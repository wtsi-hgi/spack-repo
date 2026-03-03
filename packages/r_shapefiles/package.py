# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapefiles(RPackage):
	"""Read and Write ESRI Shapefiles

	Functions to read and write ESRI shapefiles.
	"""
	
	cran = "shapefiles" 

	version("0.7.2", md5="739d7c43fee32a073b7df193f74bf1c5")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))

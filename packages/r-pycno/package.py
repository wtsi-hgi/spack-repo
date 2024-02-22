# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPycno(RPackage):
	"""Pycnophylactic Interpolation

	Given a SpatialPolygonsDataFrame and a set of populations for each polygon,
 compute a population density estimate based on Tobler's pycnophylactic interpolation
 algorithm. The result is a SpatialGridDataFrame. 
 Methods are described in Tobler Waldo R. (1979) <doi:10.1080/01621459.1979.10481647>.
	"""
	
	cran = "pycno" 

	version("1.4", md5="4cdcc3dc9d702c3cc03e059c9a3b511c")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasf(RPackage):
	"""Plot Simple Features with 'base' Sensibilities

	Resurrects the standard plot for shapes established by the
 'base' and 'graphics' packages. This is suited to workflows that require
 plotting using the established and traditional idioms of plotting spatially
 coincident data where it belongs. This package depends on 'sf' and only replaces 
 the plot method. 
	"""
	
	homepage = "https://github.com/mdsumner/basf"
	cran = "basf" 

	version("0.2.0", md5="65bfedafe9ff4a7c22383313fc5d2b25")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))

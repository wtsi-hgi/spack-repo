# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLulcc(RPackage):
	"""Land Use Change Modelling in R

	Classes and methods for spatially explicit land use change
    modelling in R.
	"""
	
	cran = "lulcc" 

	version("1.0.4", md5="b00619bec7331e602ba9d948760955fd")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))

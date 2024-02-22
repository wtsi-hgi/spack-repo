# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialepi(RPackage):
	"""Methods and Data for Spatial Epidemiology

	Methods and data for cluster detection and disease mapping.
	"""
	
	homepage = "https://github.com/rudeboybert/SpatialEpi"
	cran = "SpatialEpi" 

	version("1.2.8", md5="a8c8d837f35cbf41a55b04d86ffa813f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

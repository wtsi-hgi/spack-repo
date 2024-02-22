# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialposition(RPackage):
	"""Spatial Position Models

	Computes spatial position models: the potential model as defined
    by Stewart (1941) <doi:10.1126/science.93.2404.89> and catchment areas as
    defined by Reilly (1931) or Huff (1964) <doi:10.2307/1249154>.
	"""
	
	homepage = "https://github.com/riatelab/SpatialPosition"
	cran = "SpatialPosition" 

	version("2.1.2", md5="38a2a5a52cfd413042fcdf3a76895982")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))

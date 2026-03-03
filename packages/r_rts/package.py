# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRts(RPackage):
	"""Raster Time Series Analysis

	This framework aims to provide classes and methods for manipulating and processing of raster time series data (e.g. a time series of satellite images).
	"""
	
	homepage = "https://r-gis.net/"
	cran = "rts" 

	version("1.1-14", md5="61a9578ccf7ae7e50160bacb81f43748")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))

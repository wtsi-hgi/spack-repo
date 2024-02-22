# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpdw(RPackage):
	"""Spatial Interpolation by Inverse Path Distance Weighting

	Functions are provided to interpolate geo-referenced point data via
    Inverse Path Distance Weighting. Useful for coastal marine applications where
    barriers in the landscape preclude interpolation with Euclidean distances.
	"""
	
	homepage = "https://github.com/jsta/ipdw"
	cran = "ipdw" 

	version("2.0-0", md5="993fd735413946e8356622fc90be63fa")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))

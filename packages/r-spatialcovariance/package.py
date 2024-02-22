# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialcovariance(RPackage):
	"""Computation of Spatial Covariance Matrices for Data on
Rectangles

	Functions that compute the spatial covariance matrix for the matern and power classes of spatial models, for data that arise on rectangular units.  This code can also be used for the change of support problem and for spatial data that arise on irregularly shaped regions like counties or zipcodes by laying a fine grid of rectangles and aggregating the integrals in a form of Riemann integration.
	"""
	
	cran = "spatialCovariance" 

	version("0.6-9", md5="860b0117eb52991dd0d58e206d3f4f22")


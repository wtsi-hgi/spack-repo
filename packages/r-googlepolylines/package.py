# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglepolylines(RPackage):
	"""Encoding Coordinates into 'Google' Polylines

	Encodes simple feature ('sf') objects and coordinates, and decodes polylines 
    using the 'Google' polyline encoding algorithm (<https://developers.google.com/maps/documentation/utilities/polylinealgorithm>).
	"""
	
	cran = "googlePolylines" 

	version("0.8.4", md5="e41eaee3478c1d07b3c6abbd610d4c51")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))

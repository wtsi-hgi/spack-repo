# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodist(RPackage):
	"""Fast, Dependency-Free Geodesic Distance Calculations

	Dependency-free, ultra fast calculation of geodesic
    distances.  Includes the reference nanometre-accuracy geodesic
    distances of Karney (2013) <doi:10.1007/s00190-012-0578-z>, as used by
    the 'sf' package, as well as Haversine and Vincenty distances. Default
    distance measure is the "Mapbox cheap ruler" which is generally more
    accurate than Haversine or Vincenty for distances out to a few hundred
    kilometres, and is considerably faster. The main function accepts one
    or two inputs in almost any generic rectangular form, and returns
    either matrices of pairwise distances, or vectors of sequential
    distances.
	"""
	
	homepage = "https://github.com/hypertidy/geodist"
	cran = "geodist" 

	version("0.0.8", md5="f7c9e6a1f3469e31b5516b5228fc1351")


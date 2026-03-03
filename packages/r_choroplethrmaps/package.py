# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoroplethrmaps(RPackage):
	"""Contains Maps Used by the 'choroplethr' Package

	Contains 3 maps. 1) US States 2) US Counties 3) Countries of the
    world.
	"""
	
	homepage = "http://www.arilamstein.com/open-source"
	cran = "choroplethrMaps" 

	version("1.0.1", md5="446f79bacb472a075abd8b7741c74b5f")


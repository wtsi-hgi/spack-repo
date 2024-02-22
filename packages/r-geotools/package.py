# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeotools(RPackage):
	"""Geo tools

	Tools
	"""
	
	cran = "geotools" 

	version("0.1", md5="1859cd41d0ef57ac25e09c77f5099ec2")


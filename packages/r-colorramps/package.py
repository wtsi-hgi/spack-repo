# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorramps(RPackage):
	"""Builds Color Tables

	Builds gradient color maps.
	"""
	
	cran = "colorRamps" 

	version("2.3.4", md5="5d338c19f816ffd8f1413aebc579236f")


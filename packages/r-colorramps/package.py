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

	version("2.3.1", md5="854cb46c9d7f15cc41890ef817b23f6b")


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsetest(RPackage):
	"""Homogeneity of Stratum Effects Test

	To test the homogeneity of stratum effects in stratified paired binary data.
	"""
	
	cran = "HSEtest" 

	version("0.1.0", md5="68ec4e2f8dc62ddd4279a094db6c58ea")


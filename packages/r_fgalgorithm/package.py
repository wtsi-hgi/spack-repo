# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgalgorithm(RPackage):
	"""Flury and Gautschi algorithms

	This is a package for implementation of Flury-Gautschi
        algorithms.
	"""
	
	cran = "FGalgorithm" 

	version("1.0", md5="4928629cad8eb6b1e2e36f71e2f43d3e")


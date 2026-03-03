# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstream(RPackage):
	"""Streams of Random Numbers

	Unified object oriented interface for multiple independent streams of random numbers from different sources.
	"""
	
	homepage = "https://statmath.wu.ac.at/arvag/"
	cran = "rstream" 

	version("1.3.7", md5="daf68168cc3878be05821a72afedeeb5")

	depends_on("r@2:", type=("build", "run"))

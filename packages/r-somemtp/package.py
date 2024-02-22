# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomemtp(RPackage):
	"""Some Multiple Testing Procedures

	It's a collection of functions for Multiplicity Correction and Multiple Testing.
	"""
	
	cran = "someMTP" 

	version("1.4.1.1", md5="cd789b1f635e3eb3b2ca5e46d10d0e2d")


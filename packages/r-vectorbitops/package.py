# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVectorbitops(RPackage):
	"""Vector Bitwise Operations

	A tool for fast, efficient bitwise operations along the
    elements within a vector. Provides such functionality for AND, OR and
    XOR, as well as infix operators for all of the binary bitwise
    operations.
	"""
	
	cran = "vectorbitops" 

	version("1.1.2", md5="40829e5c304a97c9afdc120099190a28")


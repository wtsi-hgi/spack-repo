# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarver(RPackage):
	"""High Performance Colour Space Manipulation.

	The encoding of colour can be handled in many different ways, using
	different colour spaces. As different colour spaces have different uses,
	efficient conversion between these representations are important. The
	'farver' package provides a set of functions that gives access to very fast
	colour space conversion and comparisons implemented in C++, and offers
	speed improvements over the 'convertColor' function in the 'grDevices'
	package."""

	cran = "farver"

	license("MIT")

	version("2.1.1", md5="8a6b2956ba4d30911c3f2e8593eac362")


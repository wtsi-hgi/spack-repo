# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitools(RPackage):
	"""Format a number to a string with SI prefix

	Format a number (or a list of numbers) to a string (or a
        list of strings) with SI prefix. Use SI prefixes as constants
        like (4 * milli)^2
	"""
	
	cran = "sitools" 

	version("1.4", md5="41f8209e93e939dbc442015d5d01aa9b")


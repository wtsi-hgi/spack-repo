# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunes(RPackage):
	"""Convert Strings to Elder Futhark Runes

	Convert a string of text characters to Elder Futhark Runes <https://en.wikipedia.org/wiki/Elder_Futhark>.
	"""
	
	cran = "runes" 

	version("0.1.0", md5="01450f919ad74460abb46fca47fe01ef")


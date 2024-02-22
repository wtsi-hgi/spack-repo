# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYmpes(RPackage):
	"""Collection of Helper Functions

	Provides a collection of lightweight helper functions (imps) both
  for interactive use and for inclusion within other packages. These include
  functions for visualising colour palettes, quoting user input, searching rows
  of a data frame and capturing string tokens.
	"""
	
	homepage = "https://sr.ht/~tim-taylor/ympes/"
	cran = "ympes" 

	version("1.0.0", md5="38ea5b10d0c9301ed1efd7cf17f50ae3")


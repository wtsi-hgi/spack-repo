# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROz(RPackage):
	"""Plot the Australian Coastline and States

	Functions for plotting Australia's coastline and state
  boundaries.
	"""
	
	cran = "oz" 

	version("1.0-22", md5="c26f60743a98eac54a4b4198885fb114")


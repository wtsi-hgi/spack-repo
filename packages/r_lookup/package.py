# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLookup(RPackage):
	"""Functions Similar to VLOOKUP in Excel

	Simple functions to lookup items in key-value pairs. See  Mehta (2021) <doi:10.1007/978-1-4842-6613-7_6>.
	"""
	
	homepage = "https://kwstat.github.io/lookup/"
	cran = "lookup" 

	version("1.0", md5="5131f162890f60e8116287adf10396e6")


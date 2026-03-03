# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROarray(RPackage):
	"""Arrays with Arbitrary Offsets

	Generalise the starting point of the array index.
	"""
	
	cran = "Oarray" 

	version("1.4-9", md5="1cf334f881f7a1453d1bed69c7c9dd71")

	depends_on("r@3:", type=("build", "run"))

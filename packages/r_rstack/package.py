# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstack(RPackage):
	"""Stack Data Type as an 'R6' Class

	An extremely simple stack data type, implemented with 'R6'
    classes. The size of the stack increases as needed, and the amortized
    time complexity is O(1). The stack may contain arbitrary objects.
	"""
	
	homepage = "https://github.com/gaborcsardi/rstack#readme"
	cran = "rstack" 

	version("1.0.1", md5="20fa9c834829d4cbb1a83a5cf91185bc")

	depends_on("r-r6", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemofunc(RPackage):
	"""Function Memoization

	A simple way to memoize function results to improve performance by eliminating unnecessary computation or data retrieval activities.
	"""
	
	homepage = "https://github.com/rwetherall/memofunc"
	cran = "memofunc" 

	version("1.0.2", md5="bf106619c1446e09534ff861d105ce91")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

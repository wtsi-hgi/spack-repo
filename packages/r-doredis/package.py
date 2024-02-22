# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoredis(RPackage):
	"""'Foreach' Parallel Adapter Using the 'Redis' Database

	Create and manage fault-tolerant task queues for the 'foreach' package using the 'Redis' key/value database.
	"""
	
	cran = "doRedis" 

	version("3.0.2", md5="9cc29f26c68533c1269576ec5b2ce86d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreach@1.3:", type=("build", "run"))
	depends_on("r-iterators@1:", type=("build", "run"))
	depends_on("r-redux", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRando(RPackage):
	"""Context Aware Random Numbers

	Provides random number generating functions that
    are much more context aware than the built-in functions. The
    functions are also much safer, as they check for incompatible 
    values, and more reproducible. 
	"""
	
	homepage = "https://github.com/MyKo101/rando"
	cran = "rando" 

	version("0.2.0", md5="dcb5a3b20dc94820643f11ec5534a5c0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

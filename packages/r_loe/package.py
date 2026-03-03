# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoe(RPackage):
	"""Local Ordinal Embedding

	Local Ordinal embedding (LOE) is one of graph embedding methods for unweighted graphs.
	"""
	
	cran = "loe" 

	version("1.1", md5="3ebe4bf53777a50aa5431184c2ca17d9")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

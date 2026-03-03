# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobats(RPackage):
	"""An Implementation of Bat Algorithm in R

	A nature-inspired metaheuristic algorithm based on the echolocation behavior of microbats that uses frequency tuning to optimize problems in both continuous and discrete dimensions. This R package makes it easy to implement the standard bat algorithm on any user-supplied function. The algorithm was first developed by Xin-She Yang in 2010 (<DOI:10.1007/978-3-642-12538-6_6>, <DOI:10.1109/CINTI.2014.7028669>).
	"""
	
	homepage = "https://github.com/stathwang/microbats"
	cran = "microbats" 

	version("0.1-1", md5="da60beaf8662416fce7254cb98f97911")

	depends_on("r@3.2.1:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS4vd(RPackage):
	"""Biclustering via Sparse Singular Value Decomposition
Incorporating Stability Selection

	The main function s4vd() performs a biclustering via sparse
        singular value decomposition with a nested stability selection.
        The results is an biclust object and thus all methods of the
        biclust package can be applied.
	"""
	
	cran = "s4vd" 

	version("1.1-1", md5="6c1b97fa6c17ebe6dc28431f4384c356")

	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScclust(RPackage):
	"""Size-Constrained Clustering

	
    Provides wrappers for 'scclust', a C library for computationally efficient
    size-constrained clustering with near-optimal performance.
    See <https://github.com/fsavje/scclust> for more information.
	"""
	
	homepage = "https://github.com/fsavje/scclust-R"
	cran = "scclust" 

	version("0.2.4", md5="07ce20dd2f0007fbc0f1f0a2b0027f8b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))

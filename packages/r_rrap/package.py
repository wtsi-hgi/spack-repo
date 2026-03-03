# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrap(RPackage):
	"""Real-Time Adaptive Penalization for Streaming Lasso Models

	An implementation of the Real-time Adaptive Penalization (RAP) algorithm through which to iteratively update a regularization parameter in a streaming context.  
	"""
	
	cran = "rRAP" 

	version("1.1", md5="1f14a7fcd9abd73af462127d7f3a78b3")

	depends_on("r-lars", type=("build", "run"))
	depends_on("r-lassoshooting", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

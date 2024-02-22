# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROckc(RPackage):
	"""Order Constrained Solutions in k-Means Clustering

	Extends 'flexclust' with an R implementation of order constrained
  solutions in k-means clustering (Steinley and Hubert, 2008, <doi:10.1007/s11336-008-9058-z>).
	"""
	
	cran = "ockc" 

	version("1.1", md5="bf4ce7356e0dc0ac4ac9e501d09b5b38")

	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))

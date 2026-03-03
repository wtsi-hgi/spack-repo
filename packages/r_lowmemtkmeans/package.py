# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowmemtkmeans(RPackage):
	"""Low Memory Use Trimmed K-Means

	Performs the trimmed k-means clustering algorithm with lower memory use. It also provides a number of utility functions such as BIC calculations.
	"""
	
	cran = "lowmemtkmeans" 

	version("0.1.2", md5="3cd80a852cfa097e04bf561f4625cf85")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

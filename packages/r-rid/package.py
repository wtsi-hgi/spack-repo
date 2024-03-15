# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRid(RPackage):
	"""Multiple Change-Point Detection in Multivariate Time Series

	Provides efficient functions for detecting multiple change points in multidimensional time series. The models can be piecewise constant or polynomial. Adaptive threshold selection methods are available, see Fan and Wu (2024)	<arXiv:2403.00600>.
	"""
	
	cran = "rid" 

	version("0.0.1", md5="0b639a4eeab5a666c96f490b2956f5a1")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-circularsilhouette", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

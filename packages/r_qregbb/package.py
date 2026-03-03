# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQregbb(RPackage):
	"""Block Bootstrap Methods for Quantile Regression in Time Series

	Implements moving-blocks bootstrap and extended tapered-blocks bootstrap, as well as smooth versions of each, for quantile regression in time series. This package accompanies the paper: Gregory, K. B., Lahiri, S. N., & Nordman, D. J. (2018). A smooth block bootstrap for quantile regression with time series. The Annals of Statistics, 46(3), 1138-1166.
	"""
	
	cran = "QregBB" 

	version("1.0.0", md5="3246a44805157f9d601a8b50d2e484f2")

	depends_on("r-quantreg", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnsystation(RPackage):
	"""Stationarity Test Based on Unsystematic Sub-Sampling

	Performs a test for second-order stationarity of time series based
    on unsystematic sub-samples.
	"""
	
	cran = "unsystation" 

	version("0.2.0", md5="5283df0c833d1fc10ff4ba16e02bcad4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

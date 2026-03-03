# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcv(RPackage):
	"""Optimal Out-of-Sample Forecast Evaluation and Testing under
Stationarity

	Package 'ACV' (short for Affine Cross-Validation) offers an improved time-series cross-validation loss estimator which utilizes both in-sample and out-of-sample forecasting performance via a carefully constructed affine weighting scheme. Under the assumption of stationarity, the estimator is the best linear unbiased estimator of the out-of-sample loss. Besides that, the package also offers improved versions of Diebold-Mariano and Ibragimov-Muller tests of equal predictive ability which deliver more power relative to their conventional counterparts. For more information, see the accompanying article Stanek (2021) <doi:10.2139/ssrn.3996166>.
	"""
	
	cran = "ACV" 

	version("1.0.2", md5="dc783caca7b2ed8132239aa117e78919")

	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

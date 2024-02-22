# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlbdd(RPackage):
	"""Statistical Learning for Big Dependent Data

	Programs for analyzing large-scale time series data. They include functions for automatic specification and estimation of univariate time series, for clustering time series, for multivariate outlier detections, for quantile plotting of many time series, for dynamic factor models and for creating input data for deep learning programs. Examples of using the package can be found in the Wiley book 'Statistical Learning with Big Dependent Data' by Daniel Peña and Ruey S. Tsay (2021). ISBN 9781119417385.
	"""
	
	cran = "SLBDD" 

	version("0.0.4", md5="48b4c29074d6b27cc7cf94618c87c1b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-gsarima", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mts", type=("build", "run"))
	depends_on("r-tsclust", type=("build", "run"))
	depends_on("r-tsoutliers", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rnn", type=("build", "run"))

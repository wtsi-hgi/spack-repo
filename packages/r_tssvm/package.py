# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTssvm(RPackage):
	"""Time Series Forecasting using SVM Model

	Implementation and forecasting univariate time series data using the Support Vector Machine model. Support Vector Machine is one of the prominent machine learning approach for non-linear time series forecasting. For method details see Kim, K. (2003) <doi:10.1016/S0925-2312(03)00372-2>.
	"""
	
	cran = "TSSVM" 

	version("0.1.0", md5="72aefbc318f51108ae9d4e1c8d26a0e2")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))

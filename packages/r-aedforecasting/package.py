# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAedforecasting(RPackage):
	"""Change Point Analysis in ARIMA Forecasting

	Package to incorporate change point analysis in ARIMA forecasting.
	"""
	
	cran = "AEDForecasting" 

	version("0.20.0", md5="5e33062bc09002c34587d36c70aff65b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REemdarima(RPackage):
	"""EEMD Based Auto Regressive Integrated Moving Average Model

	Forecasting time series with different decomposition based ARIMA models. For method details see Yu L, Wang S, Lai KK (2008). <doi:10.1016/j.eneco.2008.05.003>. 
	"""
	
	cran = "eemdARIMA" 

	version("0.1.0", md5="fba695a06607c802d486b39c3ee39ed6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarma(RPackage):
	"""Fitting and Forecasting Gegenbauer ARMA Time Series Models

	Methods for estimating univariate long memory-seasonal/cyclical
             Gegenbauer time series processes. See for example (2022) <doi:10.1007/s00362-022-01290-3>.
             Refer to the vignette for details of fitting these processes.
	"""
	
	homepage = "https://github.com/rlph50/garma"
	cran = "garma" 

	version("0.9.13", md5="051f3e7804523e9cfd44012173c725ed")

	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-fkf", type=("build", "run"))
	depends_on("r-tswge", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNardl(RPackage):
	"""Nonlinear Cointegrating Autoregressive Distributed Lag Model

	Computes the nonlinear cointegrating autoregressive distributed lag model with automatic bases aic and bic lags selection of independent variables proposed by (Shin, Yu & Greenwood-Nimmo, 2014 <doi:10.1007/978-1-4899-8008-3_9>).
	"""
	
	homepage = "https://github.com/zedtaha/nardl"
	cran = "nardl" 

	version("0.1.6", md5="6cabae3ebf43bcf68d051912bf575445")

	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

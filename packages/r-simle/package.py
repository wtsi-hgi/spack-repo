# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimle(RPackage):
	"""Estimation and Inference for General Time Series Regression

	We provide functions for estimation and inference of nonlinear and non-stationary time series regression using the sieve methods and bootstrapping procedure. 
	"""
	
	cran = "SIMle" 

	version("0.1.0", md5="9bc3a79679ec75553440c39a02309aa4")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-sie2nts", type=("build", "run"))

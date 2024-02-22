# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPointfore(RPackage):
	"""Interpretation of Point Forecasts as State-Dependent Quantiles
and Expectiles

	Estimate specification models for the state-dependent level of an optimal quantile/expectile forecast.
  Wald Tests and the test of overidentifying restrictions are implemented. Plotting of the estimated specification model is possible.
  The package contains two data sets with forecasts and realizations: the daily accumulated precipitation at London, UK from the high-resolution model of the
  European Centre for Medium-Range Weather Forecasts (ECMWF, <https://www.ecmwf.int/>) and GDP growth Greenbook data by the US Federal Reserve.
  See Schmidt, Katzfuss and Gneiting (2015) <arXiv:1506.01917> for more details on the identification and estimation of a directive behind a point forecast.
	"""
	
	cran = "PointFore" 

	version("0.2.0", md5="25b07d7d995c2fee1f60def28d1d0618")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmooth(RPackage):
	"""Forecasting Using State Space Models

	Functions implementing Single Source of Error state space models for purposes of time series analysis and forecasting.
             The package includes ADAM (Svetunkov, 2023, <https://openforecast.org/adam/>),
             Exponential Smoothing (Hyndman et al., 2008, <doi: 10.1007/978-3-540-71918-2>),
             SARIMA (Svetunkov & Boylan, 2019 <doi: 10.1080/00207543.2019.1600764>),
             Complex Exponential Smoothing (Svetunkov & Kourentzes, 2018, <doi: 10.13140/RG.2.2.24986.29123>),
             Simple Moving Average (Svetunkov & Petropoulos, 2018 <doi: 10.1080/00207543.2017.1380326>)
             and several simulation functions. It also allows dealing with intermittent demand based on the
             iETS framework (Svetunkov & Boylan, 2019, <doi: 10.13140/RG.2.2.35897.06242>).
	"""
	
	homepage = "https://github.com/config-i1/smooth"
	cran = "smooth" 

	version("4.0.1", md5="2aa14488a3e3fa214e044ade2aba9093")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-greybox@1.0.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8.100:", type=("build", "run"))

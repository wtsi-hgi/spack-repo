# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsintermittent(RPackage):
	"""Intermittent Time Series Forecasting

	Time series methods for intermittent demand forecasting. Includes Croston's method and its variants (Moving Average, SBA), and the TSB method. Users can obtain optimal parameters on a variety of loss functions, or use fixed ones (Kourenztes (2014) <doi:10.1016/j.ijpe.2014.06.007>). Intermittent time series classification methods and iMAPA that uses multiple temporal aggregation levels are also provided (Petropoulos & Kourenztes (2015) <doi:10.1057/jors.2014.62>).
	"""
	
	homepage = "https://kourentzes.com/forecasting/2014/06/23/intermittent-demand-forecasting-package-for-r/"
	cran = "tsintermittent" 

	version("1.10", md5="024aeecc75f4f6874148265b2429c6c5")

	depends_on("r-mapa", type=("build", "run"))

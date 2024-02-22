# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsfgrnn(RPackage):
	"""Time Series Forecasting Using GRNN

	A general regression neural network (GRNN) is a variant of a
    Radial Basis Function Network characterized by a fast single-pass learning.
    'tsfgrnn' allows you to forecast time series using a GRNN model Francisco 
    Martinez et al. (2019) <doi:10.1007/978-3-030-20521-8_17> and Francisco
    Martinez et al. (2022) <doi:10.1016/j.neucom.2021.12.028>. When the forecasting
    horizon is higher than 1, two multi-step ahead forecasting strategies can be used.
    The model built is autoregressive, that is, it is only based on the 
    observations of the time series. You can consult and plot how the
    prediction was done. It is also possible to assess the forecasting accuracy
    of the model using rolling origin evaluation.
	"""
	
	homepage = "https://github.com/franciscomartinezdelrio/tsfgrnn"
	cran = "tsfgrnn" 

	version("1.0.5", md5="31a2d5e6cb2bb2b353d14d8a8eb26e57")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

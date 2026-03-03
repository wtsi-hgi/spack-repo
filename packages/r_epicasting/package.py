# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicasting(RPackage):
	"""Ewnet: An Ensemble Wavelet Neural Network for Forecasting and
Epicasting

	Method and tool for generating time series forecasts using
        an ensemble wavelet-based auto-regressive neural network architecture. This method provides
        additional support of exogenous variables and also generates confidence interval. This 
        package provides EWNet model for time series forecasting based on the algorithm by
        Panja, et al. (2022) and Panja, et al. (2023) <arXiv:2206.10696> <doi:10.1016/j.chaos.2023.113124>.          
	"""
	
	cran = "epicasting" 

	version("0.1.0", md5="58cefe14ac9b89490d4a430f7832bdc2")

	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))

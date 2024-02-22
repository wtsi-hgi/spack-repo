# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootpr(RPackage):
	"""Bootstrap Prediction Intervals and Bias-Corrected Forecasting

	Contains functions for bias-Corrected Forecasting and Bootstrap Prediction Intervals for Autoregressive Time Series.
	"""
	
	cran = "BootPR" 

	version("1.0", md5="48593b6b86d18e972a4f4b5420db1171")


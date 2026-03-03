# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllmetrics(RPackage):
	"""Calculating Multiple Performance Metrics of a Prediction Model

	Provides a function to calculate multiple performance metrics for actual and predicted values. In total eight metrics will be calculated for particular actual and predicted series. Helps to describe a Statistical model's performance in predicting a data. Also helps to compare various models' performance. The metrics are Root Mean Squared Error (RMSE), Relative Root Mean Squared Error (RRMSE), Mean absolute Error (MAE), Mean absolute percentage error (MAPE), Mean Absolute Scaled Error (MASE), Nash-Sutcliffe Efficiency (NSE), Willmott’s Index (WI), and Legates and McCabe Index (LME). Among them, first five are expected to be lesser whereas, the last three are greater the better. More details can be found from Garai and Paul (2023) <doi:10.1016/j.iswa.2023.200202> and Garai et al. (2024) <doi:10.1007/s11063-024-11552-w>.
	"""
	
	cran = "AllMetrics" 

	version("0.2.1", md5="83024ea98b0093da5151d1079a2386ac")
	version("0.2.0", md5="f3dfa360d13c451022ab4c7d936ae83c")


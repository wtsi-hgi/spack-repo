# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArigamyannsvr(RPackage):
	"""Hybrid ARIMA-GARCH and Two Specially Designed ML-Based Models

	Describes a series first. After that does time series analysis using one hybrid model and two specially structured Machine Learning (ML) (Artificial Neural Network or ANN and Support Vector Regression or SVR) models. More information can be obtained from Paul and Garai (2022) <doi:10.1007/s41096-022-00128-3>. 
	"""
	
	cran = "AriGaMyANNSVR" 

	version("0.1.0", md5="0f4e72b0f6f823415eb440f953300c02")

	depends_on("r-allmetrics", type=("build", "run"))
	depends_on("r-describedf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-fints", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-atsa", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))

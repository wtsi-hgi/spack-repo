# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaretforecast(RPackage):
	"""Conformal Time Series Forecasting Using State of Art Machine
Learning Algorithms

	Conformal time series forecasting using the caret infrastructure. 
  It provides access to state-of-the-art machine learning models for forecasting
  applications. The hyperparameter of each model is selected based on time 
  series cross-validation, and forecasting is done recursively.
	"""
	
	homepage = "https://github.com/Akai01/caretForecast"
	cran = "caretForecast" 

	version("0.1.1", md5="318740909516b0dfc3860475d8fb0bd4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-forecast@8.15:", type=("build", "run"))
	depends_on("r-caret@6.0.88:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-generics@0.1.3:", type=("build", "run"))

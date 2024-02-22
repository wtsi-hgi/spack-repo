# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreybox(RPackage):
	"""Toolbox for Model Building and Forecasting

	Implements functions and instruments for regression model building and its
             application to forecasting. The main scope of the package is in variables selection
             and models specification for cases of time series data. This includes promotional
             modelling, selection between different dynamic regressions with non-standard
             distributions of errors, selection based on cross validation, solutions to the fat
             regression model problem and more. Models developed in the package are tailored
             specifically for forecasting purposes. So as a results there are several methods
             that allow producing forecasts from these models and visualising them.
	"""
	
	homepage = "https://github.com/config-i1/greybox"
	cran = "greybox" 

	version("2.0.0", md5="233b1750f65635630a914d3cf0e79c27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

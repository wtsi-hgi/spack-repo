# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputets(RPackage):
	"""Time Series Missing Value Imputation

	Imputation (replacement) of missing values 
             in univariate time series. 
             Offers several imputation functions
             and missing data plots. 
             Available imputation algorithms include: 
            'Mean', 'LOCF', 'Interpolation', 
            'Moving Average', 'Seasonal Decomposition', 
            'Kalman Smoothing on Structural Time Series models',
            'Kalman Smoothing on ARIMA models'. Published in Moritz and Bartz-Beielstein (2017) 
            <doi:10.32614/RJ-2017-009>.
	"""
	
	homepage = "https://github.com/SteffenMoritz/imputeTS"
	cran = "imputeTS" 

	version("3.3", md5="92266787a6f8e6d4c6b49aee6aad307f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-stinepack", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

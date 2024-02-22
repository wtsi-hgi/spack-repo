# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputefin(RPackage):
	"""Imputation of Financial Time Series with Missing Values and/or
Outliers

	Missing values often occur in financial data due to a variety 
    of reasons (errors in the collection process or in the processing stage, 
    lack of asset liquidity, lack of reporting of funds, etc.). However, 
    most data analysis methods expect complete data and cannot be employed 
    with missing values. One convenient way to deal with this issue without 
    having to redesign the data analysis method is to impute the missing 
    values. This package provides an efficient way to impute the missing 
    values based on modeling the time series with a random walk or an 
    autoregressive (AR) model, convenient to model log-prices and log-volumes 
    in financial data. In the current version, the imputation is 
    univariate-based (so no asset correlation is used). In addition,
    outliers can be detected and removed.
    The package is based on the paper:
    J. Liu, S. Kumar, and D. P. Palomar (2019). Parameter Estimation of 
    Heavy-Tailed AR Model With Missing Data Via Stochastic EM. IEEE Trans. on 
    Signal Processing, vol. 67, no. 8, pp. 2159-2172. <doi:10.1109/TSP.2019.2899816>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=imputeFin"
	cran = "imputeFin" 

	version("0.1.2", md5="d4ea229bdab78e6393ba189abfb21bff")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

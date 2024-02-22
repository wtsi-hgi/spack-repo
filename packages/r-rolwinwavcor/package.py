# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolwinwavcor(RPackage):
	"""Estimate Rolling Window Wavelet Correlation Between Two Time
Series

	Estimates and plots as a heat map the rolling window wavelet correlation (RWWC) coefficients statistically significant (within the 95% CI) between two regular (evenly spaced) time series. 'RolWinWavCor' also plots at the same graphic the time series under study. The 'RolWinWavCor' was designed for financial time series, but this software can be used with other kinds of data (e.g., climatic, ecological, geological, etc). The functions contained in 'RolWinWavCor' are highly flexible since these contains some parameters to personalize the time series under analysis and the heat maps of the rolling window wavelet correlation coefficients. Moreover, we have also included a data set (named EU_stock_markets) that contains nine European stock market indices to exemplify the use of the functions contained in 'RolWinWavCor'. Methods derived from Polanco-Martínez et al (2018) <doi:10.1016/j.physa.2017.08.065>). 
	"""
	
	cran = "RolWinWavCor" 

	version("0.4.0", md5="8d262807adf875b510d2b89185197dd0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))

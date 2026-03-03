# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGldex(RPackage):
	"""Fitting Single and Mixture of Generalised Lambda Distributions

	The fitting algorithms considered in this package have two major objectives. One is to provide a smoothing device to fit distributions to data using the weight and unweighted discretised approach based on the bin width of the histogram. The other is to provide a definitive fit to the data set using the maximum likelihood and quantile matching estimation. Other methods such as moment matching, starship method, L moment matching are also provided. Diagnostics on goodness of fit can be done via qqplots, KS-resample tests and comparing mean, variance, skewness and kurtosis of the data with the fitted distribution. References include the following: Karvanen and Nuutinen (2008) "Characterizing the generalized lambda distribution by L-moments" <doi:10.1016/j.csda.2007.06.021>, King and MacGillivray (1999) "A starship method for fitting the generalised lambda distributions" <doi:10.1111/1467-842X.00089>, Su (2005) "A Discretized Approach to Flexibly Fit Generalized Lambda Distributions to Data" <doi:10.22237/jmasm/1130803560>, Su (2007) "Nmerical Maximum Log Likelihood Estimation for Generalized Lambda Distributions" <doi:10.1016/j.csda.2006.06.008>, Su (2007) "Fitting Single and Mixture of Generalized Lambda Distributions to Data via Discretized and Maximum Likelihood Methods: GLDEX in R" <doi:10.18637/jss.v021.i09>, Su (2009) "Confidence Intervals for Quantiles Using Generalized Lambda Distributions" <doi:10.1016/j.csda.2009.02.014>, Su (2010) "Chapter 14: Fitting GLDs and Mixture of GLDs to Data using Quantile Matching Method" <doi:10.1201/b10159>, Su (2010) "Chapter 15: Fitting GLD to data using GLDEX 1.0.4 in R" <doi:10.1201/b10159>, Su (2015)   "Flexible Parametric Quantile Regression Model" <doi:10.1007/s11222-014-9457-1>, Su (2021) "Flexible parametric accelerated failure time model"<doi:10.1080/10543406.2021.1934854>.
	"""
	
	cran = "GLDEX" 

	version("2.0.0.9.3", md5="3921affd180d864fc96b641e5b5e2d16")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-spacefillr", type=("build", "run"))

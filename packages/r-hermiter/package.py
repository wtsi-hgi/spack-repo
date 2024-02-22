# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHermiter(RPackage):
	"""Efficient Sequential and Batch Estimation of Univariate and
Bivariate Probability Density Functions and Cumulative
Distribution Functions along with Quantiles (Univariate) and
Nonparametric Correlation (Bivariate)

	Facilitates estimation of full univariate and bivariate 
  probability density functions and cumulative distribution functions along with
  full quantile functions (univariate) and nonparametric correlation 
  (bivariate) using Hermite series based estimators. These estimators are 
  particularly useful in the sequential setting (both stationary and 
  non-stationary) and one-pass batch estimation setting for large data sets. 
  Based on: Stephanou, Michael, Varughese, Melvin and Macdonald, Iain. "Sequential quantiles via Hermite series density estimation." Electronic Journal of Statistics 11.1 (2017): 570-607 <doi:10.1214/17-EJS1245>, 
  Stephanou, Michael and Varughese, Melvin. "On the properties of Hermite series based distribution function estimators." Metrika (2020) <doi:10.1007/s00184-020-00785-z> and Stephanou, Michael and Varughese, Melvin. "Sequential estimation of Spearman rank correlation using Hermite series estimators." Journal of Multivariate Analysis (2021) <doi:10.1016/j.jmva.2021.104783>.
	"""
	
	homepage = "https://github.com/MikeJaredS/hermiter"
	cran = "hermiter" 

	version("2.3.0", md5="c7dcb11610e765f2653bf9f581d86662")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))

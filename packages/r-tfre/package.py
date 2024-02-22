# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfre(RPackage):
	"""A Tuning-Free Robust and Efficient Approach to High-Dimensional
Regression

	Provide functions to estimate the coefficients in high-dimensional linear regressions via a tuning-free and robust approach. The method was published in Wang, L., Peng, B., Bradic, J., Li, R. and Wu, Y. (2020), "A Tuning-free Robust and Efficient Approach to High-dimensional Regression", Journal of the American Statistical Association, 115:532, 1700-1714(JASA’s discussion paper), <doi:10.1080/01621459.2020.1840989>. See also Wang, L., Peng, B., Bradic, J., Li, R. and Wu, Y. (2020), "Rejoinder to “A tuning-free robust and efficient approach to high-dimensional regression". Journal of the American Statistical Association, 115, 1726-1729, <doi:10.1080/01621459.2020.1843865>; Peng, B. and Wang, L. (2015), "An Iterative Coordinate Descent Algorithm for High-Dimensional Nonconvex Penalized Quantile Regression", Journal of Computational and Graphical Statistics, 24:3, 676-694, <doi:10.1080/10618600.2014.913516>; Clémençon, S., Colin, I., and Bellet, A. (2016), "Scaling-up empirical risk minimization: optimization of incomplete u-statistics", The Journal of Machine Learning Research, 17(1):2682–2717; Fan, J. and Li, R. (2001), "Variable Selection via Nonconcave Penalized Likelihood and its Oracle Properties", Journal of the American Statistical Association, 96:456, 1348-1360, <doi:10.1198/016214501753382273>. 
	"""
	
	cran = "TFRE" 

	version("0.1.0", md5="1ad85d1cb0ff0eb1f4621b25d241393f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

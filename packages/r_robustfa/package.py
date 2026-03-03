# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustfa(RPackage):
	"""Object Oriented Solution for Robust Factor Analysis

	Outliers virtually exist in any datasets of any application field. 
  To avoid the impact of outliers, we need to use robust estimators. 
  Classical estimators of multivariate mean and covariance matrix are 
  the sample mean and the sample covariance matrix. Outliers will 
  affect the sample mean and the sample covariance matrix, and thus 
  they will affect the classical factor analysis which depends on 
  the classical estimators (Pison, G., Rousseeuw, P.J., Filzmoser, 
  P. and Croux, C. (2003) <doi:10.1016/S0047-259X(02)00007-6>). 
  So it is necessary to use the robust estimators of the sample 
  mean and the sample covariance matrix. There are several robust 
  estimators in the literature: Minimum Covariance Determinant estimator, 
  Orthogonalized Gnanadesikan-Kettenring, Minimum Volume Ellipsoid, 
  M, S, and Stahel-Donoho. 
  The most direct way to make multivariate analysis more robust is to replace
  the sample mean and the sample covariance matrix of the classical estimators 
  to robust estimators (Maronna, R.A., Martin, D. and Yohai, V. (2006) 
  <doi:10.1002/0470010940>) (Todorov, V. and Filzmoser, P. (2009) 
  <doi:10.18637/jss.v032.i03>), which is our choice of robust factor
  analysis. We created an object oriented solution for robust factor 
  analysis based on new S4 classes. 
	"""
	
	cran = "robustfa" 

	version("1.1-0", md5="7ba0167e36adeaf7a3ba053446dee155")

	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfms(RPackage):
	"""Dynamic Factor Models

	Efficient estimation of Dynamic Factor Models using the Expectation Maximization (EM) algorithm 
  or Two-Step (2S) estimation, supporting datasets with missing data. The estimation options follow advances in the 
  econometric literature: either running the Kalman Filter and Smoother once with initial values from PCA - 
  2S estimation as in Doz, Giannone and Reichlin (2011) <doi:10.1016/j.jeconom.2011.02.012> - or via iterated 
  Kalman Filtering and Smoothing until EM convergence - following Doz, Giannone and Reichlin (2012) 
  <doi:10.1162/REST_a_00225> - or using the adapted EM algorithm of Banbura and Modugno (2014) <doi:10.1002/jae.2306>, 
  allowing arbitrary patterns of missing data. The implementation makes heavy use of the 'Armadillo' 'C++' library and 
  the 'collapse' package, providing for particularly speedy estimation. A comprehensive set of methods supports 
  interpretation and visualization of the model as well as forecasting. Information criteria to choose the number 
  of factors are also provided - following Bai and Ng (2002) <doi:10.1111/1468-0262.00273>.
	"""
	
	homepage = "https://sebkrantz.github.io/dfms/"
	cran = "dfms" 

	version("0.2.1", md5="3fe109e709952c1812fb8c08998dc8e3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-collapse@1.8:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

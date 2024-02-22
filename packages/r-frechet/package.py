# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrechet(RPackage):
	"""Statistical Analysis for Random Objects and Non-Euclidean Data

	Provides implementation of statistical methods for random objects 
    lying in various metric spaces, which are not necessarily linear spaces. 
    The core of this package is Fréchet regression for random objects with 
    Euclidean predictors, which allows one to perform regression analysis 
    for non-Euclidean responses under some mild conditions. 
    Examples include distributions in 2-Wasserstein space, 
    covariance matrices endowed with power metric (with Frobenius metric 
    as a special case), Cholesky and log-Cholesky metrics, spherical data.  
    References: Petersen, A., & Müller, H.-G. (2019) <doi:10.1214/17-AOS1624>.
	"""
	
	homepage = "https://github.com/functionaldata/tFrechet"
	cran = "frechet" 

	version("0.3.0", md5="ac920ebe13c0599e24d4fc756b5b4ca8")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fdadensity", type=("build", "run"))
	depends_on("r-fdapace@0.5.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))

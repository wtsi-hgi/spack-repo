# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarvars(RPackage):
	"""Vector Logistic Smooth Transition Models Estimation and
Prediction

	Allows the user to estimate a vector logistic smooth transition autoregressive model via maximum log-likelihood or nonlinear least squares. It further permits to test for linearity in the multivariate framework against a vector logistic smooth transition autoregressive model with a single transition variable. The estimation method is discussed in Terasvirta and Yang (2014, <doi:10.1108/S0731-9053(2013)0000031008>). Also, realized covariances can be constructed from stock market prices or returns, as explained in Andersen et al. (2001, <doi:10.1016/S0304-405X(01)00055-1>).
	"""
	
	homepage = "https://github.com/andbucci/starvars"
	cran = "starvars" 

	version("1.1.10", md5="130e5bd8ce172c4ea7991ec69856bf9a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lessr", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))

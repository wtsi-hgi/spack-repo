# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastlogisticregressionwrap(RPackage):
	"""Fast Logistic Regression Wrapper

	Provides very fast logistic regression with coefficient inferences plus other useful methods such as a forward stepwise model generator (see the benchmarks by visiting the github page at the URL below). The inputs are flexible enough to accomodate GPU computations. The coefficient estimation employs the fastLR() method in the 'RcppNumerical' package by Yixuan Qiu et al. This package allows their work to be more useful to a wider community that consumes inference.
	"""
	
	homepage = "https://github.com/kapelner/fastLogisticRegressionWrap"
	cran = "fastLogisticRegressionWrap" 

	version("1.2.0", md5="abc2e1325b9b58fbed87f391fe7313fd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

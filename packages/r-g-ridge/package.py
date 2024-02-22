# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGRidge(RPackage):
	"""Generalized Ridge Regression for Linear Models

	Ridge regression due to Hoerl and Kennard (1970)<DOI:10.1080/00401706.1970.10488634> and generalized ridge regression due to Yang and Emura (2017)<DOI:10.1080/03610918.2016.1193195> with optimized tuning parameters.
 These ridge regression estimators (the HK estimator and the YE estimator) are computed by minimizing the cross-validated mean squared errors.
 Both the ridge and generalized ridge estimators are applicable for high-dimensional regressors (p>n), where p is the number of regressors, and n is the sample size.
	"""
	
	cran = "g.ridge" 

	version("1.0", md5="a6413cfe509e5fbebea79f2274e47408")


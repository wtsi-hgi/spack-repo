# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaws(RPackage):
	"""Small-Sample Adjustments for Wald Tests Using Sandwich
Estimators

	Tests coefficients with sandwich estimator of variance and with small samples. Regression types supported are gee, linear regression, and conditional logistic regression.
	"""
	
	cran = "saws" 

	version("0.9-7.0", md5="d2a8dca5ce335511cb93aac8576d7524")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))

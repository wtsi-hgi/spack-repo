# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlms(RPackage):
	"""Non-Linear Model Selection

	Package to select best model  among several linear and nonlinear models. The main function uses the gnls() function from the 'nlme' package to fit the data to nine regression models, named: "linear", "quadratic", "cubic", "logistic", "exponential", "power", "monod", "haldane", "logit".
	"""
	
	cran = "nlMS" 

	version("1.1", md5="37cf5534fc57cd9a6b16223d88994d43")

	depends_on("r-nlme", type=("build", "run"))

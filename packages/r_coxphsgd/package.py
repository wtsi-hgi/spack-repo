# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxphsgd(RPackage):
	"""Stochastic Gradient Descent log-Likelihood Estimation in Cox
Proportional Hazards Model

	Estimate coefficients of Cox proportional hazards model using stochastic gradient descent algorithm for batch data.
	"""
	
	homepage = "https://github.com/MarcinKosinski/coxphSGD/blob/master/README.md"
	cran = "coxphSGD" 

	version("0.2.1", md5="800a6f284716751d961fffa897e9000b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalslse(RPackage):
	"""Semiparametric Least Squares Inference for Causal Effects

	Several causal effects are measured using least squares regressions and basis function approximations. Backward and forward selection methods based on different criteria are used to select the basis functions.
	"""
	
	cran = "causalSLSE" 

	version("0.3-1", md5="21c9c5268d1531270e89b6420ecdfa4d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))

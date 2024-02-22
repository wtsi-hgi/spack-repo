# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErfe(RPackage):
	"""Fits Expectile Regression for Panel Fixed Effect Model

	Fits the Expectile Regression for Fixed Effect (ERFE)
    estimator. The ERFE model extends the within-transformation strategy
    to solve the incidental parameter problem within the expectile
    regression framework. The ERFE model estimates the regressor effects
    on the expectiles of the response distribution.  The ERFE estimate
    corresponds to the classical fixed-effect within-estimator when the
    asymmetric point is 0.5. The paper by Barry, Oualkacha, and
    Charpentier (2021, <arXiv:2108.04737>) gives more details about the
    ERFE model.
	"""
	
	homepage = "https://arxiv.org/abs/2108.04737"
	cran = "erfe" 

	version("0.0.1", md5="00859a9b97d9973f2620ec0a9af79fef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

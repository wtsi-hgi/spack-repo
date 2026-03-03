# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBridgedist(RPackage):
	"""An Implementation of the Bridge Distribution with Logit-Link as
in Wang and Louis (2003)

	An implementation of the bridge distribution with logit-link in
    R. In Wang and Louis (2003) <DOI:10.1093/biomet/90.4.765>, such a univariate
    bridge distribution was derived as the distribution of the random intercept that
    'bridged' a marginal logistic regression and a conditional logistic regression.
    The conditional and marginal regression coefficients are a scalar multiple
    of each other. Such is not the case if the random intercept distribution was
    Gaussian.
	"""
	
	homepage = "https://github.com/swihart/bridgedist"
	cran = "bridgedist" 

	version("0.1.2", md5="0ee5683a3bddb286a333bcdb93c93723")

	depends_on("r@3:", type=("build", "run"))

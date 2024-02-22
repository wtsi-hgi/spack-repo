# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulaboost(RPackage):
	"""Fitting Additive Copula Regression Models for Binary Outcome
Regression

	Additive copula regression for regression
    problems with binary outcome via gradient boosting 
    [Brant, Hobæk Haff (2022); <arXiv:2208.04669>]. The fitting process
    includes a specialised model selection algorithm for each component, where
    each component is found (by greedy optimisation) among all the D-vines with
    only Gaussian pair-copulas of a fixed dimension, as specified by the user.
    When the variables and structure have been selected, the algorithm then
    re-fits the component where the pair-copula distributions can be different
    from Gaussian, if specified.
	"""
	
	cran = "copulaboost" 

	version("0.1.0", md5="0d542a8f61e320b178a0e5c1ddbb4acc")

	depends_on("r-rvinecopulib@0.5.4.1:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROglmx(RPackage):
	"""Estimation of Ordered Generalized Linear Models

	Ordered models such as ordered probit and ordered logit presume that the error variance is constant across observations. In the case that this assumption does not hold estimates of marginal effects are typically biased (Weiss (1997)). This package allows for generalization of ordered probit and ordered logit models by allowing the user to specify a model for the variance. Furthermore, the package includes functions to calculate the marginal effects. Wrapper functions to estimate the standard limited dependent variable models are also included.
	"""
	
	cran = "oglmx" 

	version("3.0.0.0", md5="b0376b0eba0cf00bbcb6c9c75f7fc52c")

	depends_on("r-maxlik", type=("build", "run"))

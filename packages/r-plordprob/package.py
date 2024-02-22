# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlordprob(RPackage):
	"""Multivariate Ordered Probit Model via Pairwise Likelihood

	Multivariate ordered probit model, i.e. the extension of the scalar ordered probit model where the observed variables have dimension greater than one. Estimation of the parameters is done via maximization of the pairwise likelihood, a special case of the composite likelihood obtained as product of bivariate marginal distributions. The package uses the Fortran 77 subroutine SADMVN by Alan Genz, with minor adaptations made by Adelchi Azzalini in his "mvnormt" package for evaluating the two-dimensional Gaussian integrals involved in the pairwise log-likelihood. Optimization of the latter objective function  is performed via quasi-Newton box-constrained optimization algorithm, as implemented in nlminb.
	"""
	
	cran = "PLordprob" 

	version("1.1", md5="c417c8c79cb91daaaa707093f10906bb")

	depends_on("r-mnormt", type=("build", "run"))

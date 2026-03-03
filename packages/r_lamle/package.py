# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLamle(RPackage):
	"""Maximum Likelihood Estimation of Latent Variable Models

	Approximate marginal maximum likelihood estimation of multidimensional
	latent variable models via adaptive quadrature or Laplace approximations to the 
	integrals in the likelihood function, as presented for confirmatory factor 
	analysis models in Jin, S., Noh, M., and Lee, Y. (2018) 
	<doi:10.1080/10705511.2017.1403287>, for item response theory models in 
	Andersson, B., and Xin, T. (2021) <doi:10.3102/1076998620945199>, and for 
	generalized linear latent variable models in Andersson, B., Jin, S., and 
	Zhang, M. (2023) <doi:10.1016/j.csda.2023.107710>. Models implemented include
	the generalized	partial credit model, the graded response model, and generalized 
	linear latent variable models for Poisson, negative-binomial and normal 
	distributions. Supports a combination of binary, ordinal, count and continuous 
	observed variables and multiple	group models.
	"""
	
	cran = "lamle" 

	version("0.3.1", md5="d4ebf736137fae552f611b4e9e5916bd")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

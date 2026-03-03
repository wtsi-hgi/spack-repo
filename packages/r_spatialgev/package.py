# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialgev(RPackage):
	"""Fit Spatial Generalized Extreme Value Models

	Fit latent variable models with the GEV distribution as the data likelihood and the GEV parameters following latent Gaussian processes. The models in this package are built using the template model builder 'TMB' in R, which has the fast ability to integrate out the latent variables using Laplace approximation. This package allows the users to choose in the fit function which GEV parameter(s) is considered as a spatially varying random effect following a Gaussian process, so the users can fit spatial GEV models with different complexities to their dataset without having to write the models in 'TMB' by themselves. This package also offers methods to sample from both fixed and random effects posteriors as well as the posterior predictive distributions at different spatial locations. Methods for fitting this class of models are described in Chen, Ramezan, and Lysy (2021) <arXiv:2110.07051>.
	"""
	
	cran = "SpatialGEV" 

	version("1.0.0", md5="fef9b3b78248aad1ef3ce37baa43e66b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))

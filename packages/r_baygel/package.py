# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaygel(RPackage):
	"""Bayesian Shrinkage Estimators for Precision Matrices in Gaussian
Graphical Models

	This R package offers block Gibbs samplers for the Bayesian (adaptive) graphical lasso, ridge, and naive elastic net priors. These samplers facilitate the simulation of the posterior distribution of precision matrices for Gaussian distributed data and were originally proposed by: Wang (2012) <doi:10.1214/12-BA729>; Smith et al. (2022) <doi:10.48550/arXiv.2210.16290> and Smith et al. (2023) <doi:10.48550/arXiv.2306.14199>, respectively.
	"""
	
	homepage = "https://github.com/Jarod-Smithy/baygel"
	cran = "baygel" 

	version("0.3.0", md5="739b37a01222b1afc0d1c4e6aed8dad7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))

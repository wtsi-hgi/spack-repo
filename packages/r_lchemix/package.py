# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLchemix(RPackage):
	"""A Bayesian Multi-Dimensional Couple-Based Latent Risk Model

	A joint latent class model where a hierarchical structure exists, with an interaction between female and male partners of a couple. A Bayesian perspective to inference and Markov chain Monte Carlo algorithms to obtain posterior estimates of model parameters. The reference paper is: Beom Seuk Hwang, Zhen Chen, Germaine M.Buck Louis, Paul S. Albert, (2018) "A Bayesian multi-dimensional couple-based latent risk model with an application to infertility". Biometrics, 75, 315-325. <doi:10.1111/biom.12972>.
	"""
	
	homepage = "http://github.com/wzhang17/lchemix.git"
	cran = "lchemix" 

	version("0.1.0", md5="c19bd4fbe637527d8b3180077b4acc48")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

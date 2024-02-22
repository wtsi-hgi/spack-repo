# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSahpm(RPackage):
	"""Variable Selection using Simulated Annealing

	Highest posterior model is widely accepted as a good model among available models. In terms of variable selection highest posterior model is often the true model. Our stochastic search process SAHPM based on simulated annealing maximization method tries to find the highest posterior model by maximizing the model space with respect to the posterior probabilities of the models. This package currently contains the SAHPM method only for linear models. The codes for GLM will be added in future.
	"""
	
	cran = "sahpm" 

	version("1.0.1", md5="f730b525940cd532d2d19217e102c5e9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

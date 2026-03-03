# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPogit(RPackage):
	"""Bayesian Variable Selection for a Poisson-Logistic Model

	Bayesian variable selection for regression models of under-reported
    count data as well as for (overdispersed) Poisson, negative binomal and
    binomial logit regression models using spike and slab priors.
	"""
	
	cran = "pogit" 

	version("1.3.0", md5="37c43aab49b9b537040567310a041d58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

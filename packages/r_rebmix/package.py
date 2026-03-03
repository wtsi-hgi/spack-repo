# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebmix(RPackage):
	"""Finite Mixture Modeling, Clustering & Classification

	Random univariate and multivariate finite mixture model generation, estimation, clustering, latent class analysis and classification. Variables can be continuous, discrete, independent or dependent and may follow normal, lognormal, Weibull, gamma, Gumbel, binomial, Poisson, Dirac, uniform or circular von Mises parametric families.
	"""
	
	cran = "rebmix" 

	version("2.15.0", md5="c94f35f79b58d5c7210a08bdec34a9a9")

	depends_on("r@3.1:", type=("build", "run"))

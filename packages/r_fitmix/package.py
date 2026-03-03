# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitmix(RPackage):
	"""Finite Mixture Model Fitting of Lifespan Datasets

	Fits the lifespan datasets of biological systems such as yeast, fruit flies, and other similar biological units with well-known finite mixture models introduced by Farewell V. (1982) <doi:10.2307/2529885> and Al-Hussaini et al. (2000) <doi:10.1080/00949650008812033>. Estimates parameter space fitting of a lifespan dataset with finite mixtures of parametric distributions. Computes the following tasks; 1) Estimates parameter space of the finite mixture model 
             by implementing the expectation maximization (EM) algorithm. 2) Finds a sequence of four goodness-of-fit measures consist of Akaike Information Criterion (AIC), Bayesian Information Criterion (BIC), Kolmogorov-Smirnov (KS), and log-likelihood (log-likelihood) statistics. 3)The initial values is determined by k-means clustering.
	"""
	
	homepage = "https://github.com/guven-code/fitmix/"
	cran = "fitmix" 

	version("0.1.0", md5="1ec8894edbbbd4c0a93af1825ed03ab0")

	depends_on("r@3.1:", type=("build", "run"))

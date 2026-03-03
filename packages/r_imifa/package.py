# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImifa(RPackage):
	"""Infinite Mixtures of Infinite Factor Analysers and Related
Models

	Provides flexible Bayesian estimation of Infinite Mixtures of Infinite Factor Analysers and related models, for nonparametrically clustering high-dimensional data, introduced by Murphy et al. (2020) <doi:10.1214/19-BA1179>. The IMIFA model conducts Bayesian nonparametric model-based clustering with factor analytic covariance structures without recourse to model selection criteria to choose the number of clusters or cluster-specific latent factors, mostly via efficient Gibbs updates. Model-specific diagnostic tools are also provided, as well as many options for plotting results, conducting posterior inference on parameters of interest, posterior predictive checking, and quantifying uncertainty.
	"""
	
	homepage = "https://cran.r-project.org/package=IMIFA"
	cran = "IMIFA" 

	version("2.2.0", md5="e249699dc538624b3f7d930ee6e8bdf5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrixstats@1:", type=("build", "run"))
	depends_on("r-mclust@5.4:", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rfast@1.9.8:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))

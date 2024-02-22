# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesm(RPackage):
	"""Bayesian Inference for Marketing/Micro-Econometrics.

	Covers many important models used in marketing and micro-econometrics
	applications.  The package includes: Bayes Regression (univariate or
	multivariate dep var), Bayes Seemingly Unrelated Regression (SUR), Binary
	and Ordinal Probit, Multinomial Logit (MNL) and Multinomial Probit (MNP),
	Multivariate Probit, Negative Binomial (Poisson) Regression, Multivariate
	Mixtures of Normals (including clustering), Dirichlet Process Prior Density
	Estimation with normal base, Hierarchical Linear Models with normal prior
	and covariates, Hierarchical Linear Models with a mixture of normals prior
	and covariates, Hierarchical Multinomial Logits with a mixture of normals
	prior and covariates, Hierarchical Multinomial Logits with a Dirichlet
	Process prior and covariates, Hierarchical Negative Binomial Regression
	Models, Bayesian analysis of choice-based conjoint data, Bayesian treatment
	of linear instrumental variables models, Analysis of Multivariate Ordinal
	survey data with scale usage heterogeneity (as in Rossi et al, JASA (01)),
	Bayesian Analysis of Aggregate Random Coefficient Logit Models as in BLP
	(see Jiang, Manchanda, Rossi 2009) For further reference, consult our book,
	Bayesian Statistics and Marketing by Rossi, Allenby and McCulloch (Wiley
	2005) and Bayesian Non- and Semi-Parametric Methods and Applications
	(Princeton U Press 2014)."""

	cran = "bayesm"

	version("3.1-6", md5="3ce1e250505c319ef9b0b9b113cfead8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

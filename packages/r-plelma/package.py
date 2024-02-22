# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlelma(RPackage):
	"""Pseudo-Likelihood Estimation of Log-Multiplicative Association
Models

	Log-multiplicative association models (LMA) are
    models for cross-classifications of categorical variables
    where interactions are represented by products of category
    scale values and an association parameter. Maximum
    likelihood estimation (MLE) fails for moderate to large
    numbers of categorical variables. The 'pleLMA' package
    overcomes this limitation of MLE by using pseudo-likelihood
    estimation to fit the models to small or large
    cross-classifications dichotomous or multi-category variables.
    Originally proposed by Besag (1974,
    <doi:10.1111/j.2517-6161.1974.tb00999.x>), pseudo-likelihood
    estimation takes large complex models and breaks it down
    into smaller ones. Rather than maximizing the likelihood
    of the joint distribution of all the variables, a
    pseudo-likelihood function, which is the product likelihoods
    from conditional distributions, is maximized. LMA models can
    be derived from a number of different frameworks including
    (but not limited to) graphical models and uni-dimensional
    and multi-dimensional item response theory models. More
    details about the models and estimation can be found in
    the vignette.
	"""
	
	cran = "pleLMA" 

	version("0.2.1", md5="52a9651d6ab638b43ee67a20e30efdbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))

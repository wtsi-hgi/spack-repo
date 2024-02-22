# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBas(RPackage):
	"""Bayesian Variable Selection and Model Averaging using Bayesian
Adaptive Sampling

	Package for Bayesian Variable Selection and  Model Averaging 
    in linear models and generalized linear models using stochastic or
    deterministic sampling without replacement from posterior
    distributions.  Prior distributions on coefficients are
    from Zellner's g-prior or mixtures of g-priors
    corresponding to the Zellner-Siow Cauchy Priors or the
    mixture of g-priors from Liang et al (2008)
    <DOI:10.1198/016214507000001337>
    for linear models or mixtures of g-priors from  Li and Clyde
    (2019) <DOI:10.1080/01621459.2018.1469992> in generalized linear models.
    Other model selection criteria include AIC, BIC and Empirical Bayes 
    estimates of g. Sampling probabilities may be updated based on the sampled
    models using sampling w/out replacement or an efficient MCMC algorithm which
    samples models using a tree structure of the model space 
    as an efficient hash table.  See  Clyde, Ghosh and Littman (2010) 
    <DOI:10.1198/jcgs.2010.09049> for  details on the sampling algorithms.
    Uniform priors over all models or beta-binomial prior distributions on
    model size are allowed, and for large p truncated priors on the model
    space may be used to enforce sampling models that are full rank.  
    The user may force variables to always be included in addition to imposing
    constraints that higher order interactions are included only if their 
    parents are included in the model.
    This material is based upon work supported by the National Science
    Foundation under Division of Mathematical Sciences grant 1106891.
    Any opinions, findings, and
    conclusions or recommendations expressed in this material are those of
    the author(s) and do not necessarily reflect the views of the
    National Science Foundation.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "BAS" 

	version("1.7.1", md5="1c325a61bcf14763745821d716cc844d")

	depends_on("r@3:", type=("build", "run"))

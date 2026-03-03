# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvsnlp(RPackage):
	"""Bayesian Variable Selection in High Dimensional Settings using
Nonlocal Priors

	Variable/Feature selection in high or ultra-high dimensional
    settings has gained a lot of attention recently specially in cancer genomic
    studies. This package provides a Bayesian approach to tackle this problem,
    where it exploits mixture of point masses at zero and nonlocal priors to
    improve the performance of variable selection and coefficient estimation.
    product moment (pMOM) and product inverse moment (piMOM) nonlocal priors
    are implemented and can be used for the analyses. This package performs
    variable selection for binary response and survival time response datasets
    which are widely used in biostatistic and bioinformatics community.
    Benefiting from parallel computing ability, it reports necessary outcomes
    of Bayesian variable selection such as Highest Posterior Probability Model
    (HPPM), Median Probability Model (MPM) and posterior inclusion probability
    for each of the covariates in the model. The option to use Bayesian Model
    Averaging (BMA) is also part of this package that can be exploited for
    predictive power measurements in real datasets.
	"""
	
	cran = "BVSNLP" 

	version("1.1.9", md5="0db5fac2f93a24ea204617b547b1fd12")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))

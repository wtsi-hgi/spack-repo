# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBqror(RPackage):
	"""Bayesian Quantile Regression for Ordinal Models

	Package provides functions for estimation and inference in Bayesian quantile regression with ordinal outcomes. An ordinal model with 3 or more outcomes (labeled OR1 model) is estimated by a combination of Gibbs sampling and Metropolis-Hastings (MH) algorithm. Whereas an ordinal model with exactly 3 outcomes (labeled OR2 model) is estimated using a Gibbs sampling algorithm. The summary output presents the posterior mean, posterior standard deviation, 95% credible intervals, and the inefficiency factors along with the two model comparison measures – logarithm of marginal likelihood and the deviance information criterion (DIC). The package also provides functions for computing the covariate effects and other functions that aids either the estimation or inference in quantile ordinal models.
    Rahman, M. A. (2016).“Bayesian Quantile Regression for Ordinal Models.” Bayesian Analysis, 11(1): 1-24 <doi: 10.1214/15-BA939>.
    Yu, K., and Moyeed, R. A. (2001). “Bayesian Quantile Regression.” Statistics and Probability Letters, 54(4): 437–447 <doi: 10.1016/S0167-7152(01)00124-9>.
    Koenker, R., and Bassett, G. (1978).“Regression Quantiles.” Econometrica, 46(1): 33-50 <doi: 10.2307/1913643>.
    Chib, S. (1995). “Marginal likelihood from the Gibbs output.” Journal of the American Statistical Association, 90(432):1313–1321, 1995. <doi: 10.1080/01621459.1995.10476635>.
    Chib, S., and Jeliazkov, I. (2001). “Marginal likelihood from the Metropolis-Hastings output.” Journal of the American Statistical Association, 96(453):270–281, 2001. <doi: 10.1198/016214501750332848>.
	"""
	
	homepage = "https://github.com/prajual/bqror"
	cran = "bqror" 

	version("1.6.1", md5="b2ae5bbcc88296f41aa3437f7e60e5ef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-npflow", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))

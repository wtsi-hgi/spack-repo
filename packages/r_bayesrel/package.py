# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrel(RPackage):
	"""Bayesian Reliability Estimation

	Functionality for reliability estimates. For 'unidimensional' tests:
    Coefficient alpha, 'Guttman's' lambda-2/-4/-6, the Greatest lower
    bound and coefficient omega_u ('unidimensional') in a Bayesian and a frequentist version. 
    For multidimensional tests: omega_t (total) and omega_h (hierarchical). 
    The results include confidence and credible intervals, the 
    probability of a coefficient being larger than a cutoff, 
    and a check for the factor models, necessary for the omega coefficients. 
    The method for the Bayesian 'unidimensional' estimates, except for omega_u, 
    is sampling from the posterior inverse 'Wishart' for the 
    covariance matrix based measures (see 'Murphy', 2007, 
    <https://groups.seas.harvard.edu/courses/cs281/papers/murphy-2007.pdf>. 
    The Bayesian omegas (u, t, and h) are obtained by 
    'Gibbs' sampling from the conditional posterior distributions of 
    (1) the single factor model, (2) the second-order factor model, (3) the bi-factor model, 
    (4) the correlated factor model
    ('Lee', 2007, <doi:10.1002/9780470024737>). 
	"""
	
	homepage = "https://github.com/juliuspfadt/Bayesrel"
	cran = "Bayesrel" 

	version("0.7.7", md5="a2132d9a32d7c0e34de564455f6ca216")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

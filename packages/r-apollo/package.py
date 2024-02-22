# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApollo(RPackage):
	"""Tools for Choice Model Estimation and Application

	Choice models are a widely used technique across numerous scientific disciplines. The Apollo package is a very flexible tool for the estimation and application 
    of choice models in R. Users are able to write their own 
    model functions or use a mix of already available ones. Random heterogeneity, 
    both continuous and discrete and at the level of individuals and 
    choices, can be incorporated for all models. There is support for both standalone 
    models and hybrid model structures.  Both classical 
    and Bayesian estimation is available, and multiple discrete 
    continuous models are covered in addition to discrete choice. 
    Multi-threading processing is supported for estimation and a large
    number of pre and post-estimation routines, including for computing posterior
    (individual-level) distributions are available. 
    For examples, a manual, and a support forum, visit 
    <http://www.ApolloChoiceModelling.com>. For more information on choice 
    models see Train, K. (2009) <isbn:978-0-521-74738-7> and Hess, 
    S. & Daly, A.J. (2014) <isbn:978-1-781-00314-5> for an overview 
    of the field.
	"""
	
	homepage = "http://www.apolloChoiceModelling.com"
	cran = "apollo" 

	version("0.3.1", md5="c29ef962faf721aa39df3658f670c2a1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rsghb", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bgw@0.1.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

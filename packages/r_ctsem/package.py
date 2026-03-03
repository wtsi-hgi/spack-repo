# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtsem(RPackage):
	"""Continuous Time Structural Equation Modelling

	Hierarchical continuous (and discrete) time state space modelling, for linear
    and nonlinear systems measured by  continuous variables, with limited support for 
    binary data. The subject specific dynamic system is modelled as a stochastic 
    differential equation (SDE) or difference equation, measurement models are typically multivariate normal factor models. 
    Linear mixed effects SDE's estimated via maximum likelihood and optimization are the default.
    Nonlinearities,  (state dependent parameters) and random effects on all parameters
    are possible, using either max likelihood / max a posteriori optimization 
    (with optional importance sampling) or Stan's Hamiltonian Monte Carlo sampling. 
    See  <https://github.com/cdriveraus/ctsem/raw/master/vignettes/hierarchicalmanual.pdf>
    for details. Priors may be used. For the conceptual overview of the hierarchical Bayesian 
    linear SDE approach, 
    see <https://www.researchgate.net/publication/324093594_Hierarchical_Bayesian_Continuous_Time_Dynamic_Modeling>.
    Exogenous inputs may also be included, for an overview of such possibilities see <https://www.researchgate.net/publication/328221807_Understanding_the_Time_Course_of_Interventions_with_Continuous_Time_Dynamic_Models> .
    Stan based functions are not available on 32 bit Windows systems at present. 
    <https://cdriver.netlify.app/> contains some tutorial blog posts.
	"""
	
	homepage = "https://github.com/cdriveraus/ctsem"
	cran = "ctsem" 

	version("3.9.1", md5="beaf5975f5f69ad24f20d3d04ec88d3d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.16:", type=("build", "run"))
	depends_on("r-code", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mize", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))

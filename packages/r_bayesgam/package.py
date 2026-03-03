# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgam(RPackage):
	"""Fit Multivariate Response Generalized Additive Models using
Hamiltonian Monte Carlo

	The 'bayesGAM' package is designed to provide a user friendly option to fit univariate and multivariate response Generalized Additive Models (GAM) using Hamiltonian Monte Carlo (HMC) with few technical burdens.  The functions in this package use 'rstan' (Stan Development Team 2020)  to call 'Stan' routines that run the HMC simulations. The 'Stan' code for these models is already pre-compiled for the user. The programming formulation for models in 'bayesGAM' is designed to be familiar to analysts who fit statistical models in 'R'.
    Carpenter, B., Gelman, A., Hoffman, M. D., Lee, D., Goodrich, B., Betancourt, M., ... & Riddell, A. (2017). Stan: A probabilistic programming language. Journal of statistical software, 76(1). 
    Stan Development Team. 2018. RStan: the R interface to Stan. R package version 2.17.3.   <https://mc-stan.org/>
    Neal, Radford (2011) "Handbook of Markov Chain Monte Carlo" ISBN: 978-1420079418.
    Betancourt, Michael, and Mark Girolami. "Hamiltonian Monte Carlo for hierarchical models." Current trends in Bayesian methodology with applications 79.30 (2015): 2-4.
    Thomas, S., Tu, W. (2020) "Learning Hamiltonian Monte Carlo in R" <arXiv:2006.16194>,
    Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013) "Bayesian Data Analysis" ISBN: 978-1439840955, 
    Agresti, Alan (2015) "Foundations of Linear and Generalized Linear Models ISBN: 978-1118730034, 
    Pinheiro, J., Bates, D. (2006) "Mixed-effects Models in S and S-Plus" ISBN: 978-1441903174.
    Ruppert, D., Wand, M. P., & Carroll, R. J. (2003). Semiparametric regression (No. 12). Cambridge university press. ISBN: 978-0521785167.
	"""
	
	cran = "bayesGAM" 

	version("0.0.2", md5="266631b677116cfb174f82d4c8797072")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.0.9000:", type=("build", "run"))
	depends_on("r-semipar", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))

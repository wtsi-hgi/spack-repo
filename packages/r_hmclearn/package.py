# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmclearn(RPackage):
	"""Fit Statistical Models Using Hamiltonian Monte Carlo

	Provide users with a framework to learn the intricacies of the Hamiltonian Monte Carlo algorithm with hands-on experience by tuning and fitting their own models.  All of the code is written in R.  Theoretical references are listed below:.
    Neal, Radford (2011) "Handbook of Markov Chain Monte Carlo" ISBN: 978-1420079418, 
    Betancourt, Michael (2017) "A Conceptual Introduction to Hamiltonian Monte Carlo" <arXiv:1701.02434>, 
    Thomas, S., Tu, W. (2020) "Learning Hamiltonian Monte Carlo in R" <arXiv:2006.16194>,
    Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013) "Bayesian Data Analysis" ISBN: 978-1439840955, 
    Agresti, Alan (2015) "Foundations of Linear and Generalized Linear Models ISBN: 978-1118730034, 
    Pinheiro, J., Bates, D. (2006) "Mixed-effects Models in S and S-Plus" ISBN: 978-1441903174.
	"""
	
	cran = "hmclearn" 

	version("0.0.5", md5="c5a65d39ec3834fecb1c1bfe23a9a1de")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanple(RPackage):
	"""Fitting Shared Atoms Nested Models via Markov Chains Monte Carlo

	Estimate Bayesian nested mixture models via Markov Chain Monte Carlo methods. Specifically, the package implements the common atoms model (Denti et al., 2023), its finite version (D'Angelo et al., 2023), and a hybrid finite-infinite model. 
             All models use Gaussian mixtures with a normal-inverse-gamma prior distribution on the parameters. Additional functions are provided to help analyzing the results of the fitting procedure.  
             References:  
             Denti, Camerlenghi, Guindani, Mira (2023) <doi:10.1080/01621459.2021.1933499>,   
             D’Angelo, Canale, Yu, Guindani (2023) <doi:10.1111/biom.13626>.
	"""
	
	homepage = "https://github.com/laura-dangelo/SANple"
	cran = "SANple" 

	version("0.1.0", md5="898c6204dcfe3ff259c429aedf12f824")

	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-salso", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepbvs(RPackage):
	"""Bayesian Variable Selection using Power-Expected-Posterior Prior

	Performs Bayesian variable selection under normal linear
          models for the data with the model parameters following as prior either 
          the power-expected-posterior (PEP) or the intrinsic (a special case of the former)
          (Fouskakis and Ntzoufras (2022) <doi: 10.1214/21-BA1288>,
          Fouskakis and Ntzoufras (2020) <doi: 10.3390/econometrics8020017>).          
          The prior distribution on model space is the uniform on model space
          or the uniform on model dimension (a special case of the beta-binomial prior). 
          The selection can be done either with full enumeration of all 
          possible models or using the Markov Chain Monte Carlo Model Composition (MC3) 
          algorithm (Madigan and York (1995) <doi: 10.2307/1403615>). 
          Complementary functions for making predictions, as well as plotting and 
          printing the results are also provided.
	"""
	
	cran = "PEPBVS" 

	version("1.0", md5="143798efeef91284596c0eb11c0c8302")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))

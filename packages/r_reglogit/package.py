# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReglogit(RPackage):
	"""Simulation-Based Regularized Logistic Regression

	Regularized (polychotomous) logistic regression 
  by Gibbs sampling. The package implements subtly different 
  MCMC schemes with varying efficiency depending on the data type 
  (binary v. binomial, say) and the desired estimator (regularized maximum
  likelihood, or Bayesian maximum a posteriori/posterior mean, etc.) through a 
  unified interface. For details, see Gramacy & Polson (2012 <doi:10.1214/12-BA719>).
	"""
	
	homepage = "https://bobby.gramacy.com/r_packages/reglogit/"
	cran = "reglogit" 

	version("1.2-7", md5="0d9c621d4df53c3d7c80ca062caea1fe")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

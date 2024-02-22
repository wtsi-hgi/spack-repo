# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoomspikeslab(RPackage):
	"""MCMC for Spike and Slab Regression

	Spike and slab regression with a variety of residual error
  distributions corresponding to Gaussian, Student T, probit, logit, SVM, and a
  few others.  Spike and slab regression is Bayesian regression with prior
  distributions containing a point mass at zero.  The posterior updates the
  amount of mass on this point, leading to a posterior distribution that is
  actually sparse, in the sense that if you sample from it many coefficients are
  actually zeros.  Sampling from this posterior distribution is an elegant way
  to handle Bayesian variable selection and model averaging.  See
  <DOI:10.1504/IJMMNO.2014.059942> for an explanation of the Gaussian case.
	"""
	
	cran = "BoomSpikeSlab" 

	version("1.2.6", md5="214eb2fc654fe6e98723c7db7008ec23")

	depends_on("r-boom@0.9.13:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))

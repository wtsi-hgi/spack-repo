# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrum(RPackage):
	"""Bayesian Estimation of the Reduced Reparameterized Unified Model
with Gibbs Sampling

	Implementation of Gibbs sampling algorithm for Bayesian Estimation
    of the Reduced Reparameterized Unified Model ('rrum'), described by 
    Culpepper and Hudson (2017) <doi: 10.1177/0146621617707511>.
	"""
	
	homepage = "https://tmsalab.github.io/rrum/"
	cran = "rrum" 

	version("0.2.1", md5="339039f0afd0ac3e707bdda6d5a72e84")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-simcdm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.12.6.6:", type=("build", "run"))
	depends_on("r-rgen", type=("build", "run"))

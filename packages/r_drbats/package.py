# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrbats(RPackage):
	"""Data Representation: Bayesian Approach That's Sparse

	Feed longitudinal data into a Bayesian Latent Factor Model to obtain 
  a low-rank representation. Parameters are estimated using a Hamiltonian 
  Monte Carlo algorithm with STAN. See G. Weinrott, B. Fontez, N. Hilgert and 
  S. Holmes, "Bayesian Latent Factor Model for Functional Data Analysis", 
  Actes des JdS 2016.
	"""
	
	cran = "DrBats" 

	version("0.1.6", md5="2d336b15c1b9f5f7c207ed771ab7ed2e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sde", type=("build", "run"))

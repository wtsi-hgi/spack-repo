# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeastjar(RPackage):
	"""JAR Dependency for MCMC Using 'BEAST'

	Provides JAR to perform Markov chain Monte Carlo (MCMC) inference using
    the popular Bayesian Evolutionary Analysis by Sampling Trees 'BEAST' software library
    of Suchard et al (2018) <doi:10.1093/ve/vey016>. 'BEAST' supports auto-tuning
    Metropolis-Hastings, slice, Hamiltonian Monte Carlo and Sequential Monte Carlo
    sampling for a large variety of composable standard and phylogenetic statistical
    models using high performance computing.  By placing the 'BEAST' JAR in this package,
    we offer an efficient distribution system for 'BEAST' use by other R packages using
    CRAN.
	"""
	
	homepage = "https://github.com/beast-dev/BeastJar"
	cran = "BeastJar" 

	version("1.10.6", md5="d05b4d4b704c99c53f6aa7bbc37d7cb9")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))

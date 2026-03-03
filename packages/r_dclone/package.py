# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDclone(RPackage):
	"""Data Cloning and MCMC Tools for Maximum Likelihood Methods

	Low level functions for implementing
    maximum likelihood estimating procedures for
    complex models using data cloning and Bayesian
    Markov chain Monte Carlo methods
    as described in Solymos 2010 <doi:10.32614/RJ-2010-011>.
    Sequential and parallel MCMC support
    for 'JAGS', 'WinBUGS', 'OpenBUGS', and 'Stan'.
	"""
	
	homepage = "https://groups.google.com/forum/#!forum/dclone-users"
	cran = "dclone" 

	version("2.3-2", md5="38676c0e50cef63f8fe03cce232cb69d")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rjags@4.4:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-r2openbugs", type=("build", "run"))
	depends_on("jags@3.0.0:", type=("build", "link", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPotts(RPackage):
	"""Markov Chain Monte Carlo for Potts Models

	Do Markov chain Monte Carlo (MCMC) simulation of Potts models
   (Potts, 1952, <doi:10.1017/S0305004100027419>),
   which are the multi-color generalization of Ising models
   (so, as as special case, also simulates Ising models).
   Use the Swendsen-Wang algorithm (Swendsen and Wang, 1987,
   <doi:10.1103/PhysRevLett.58.86>) so MCMC is fast.
   Do maximum composite likelihood estimation of parameters
   (Besag, 1975, <doi:10.2307/2987782>,
   Lindsay, 1988, <doi:10.1090/conm/080>).
	"""
	
	homepage = "http://www.stat.umn.edu/geyer/mcmc/"
	cran = "potts" 

	version("0.5-11", md5="017c38f7b58cc24c3584e48b992debfc")

	depends_on("r@3.6:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoa(RPackage):
	"""Bayesian Output Analysis Program (BOA) for MCMC

	A menu-driven program and library of functions for carrying out
    convergence diagnostics and statistical and graphical analysis of Markov
    chain Monte Carlo sampling output.
	"""
	
	homepage = "http://www.jstatsoft.org/v21/i11"
	cran = "boa" 

	version("1.1.8-2", md5="a2391bcb7087201dc4e1de5d1ab97d2c")

	depends_on("r@2.7:", type=("build", "run"))

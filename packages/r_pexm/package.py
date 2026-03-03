# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPexm(RPackage):
	"""Loading a JAGS Module for the Piecewise Exponential Distribution

	Load the Just Another Gibbs Sampling (JAGS) module 'pexm'. The module provides the tools to work with the Piecewise Exponential (PE) distribution in a Bayesian model with the corresponding Markov Chain Monte Carlo algorithm (Gibbs Sampling) implemented via JAGS. Details about the module implementation can be found in Mayrink et al. (2021) <doi:10.18637/jss.v100.i08>.
	"""
	
	homepage = "https://github.com/vdinizm/pexm"
	cran = "pexm" 

	version("1.1.3", md5="cda12b7866e135aea287ad3a3e3d7a84")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))

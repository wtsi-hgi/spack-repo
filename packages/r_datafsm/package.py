# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatafsm(RPackage):
	"""Estimating Finite State Machine Models from Data

	Automatic generation of finite state machine models of dynamic 
    decision-making that both have strong predictive power and are 
    interpretable in human terms. We use an efficient model representation and 
    a genetic algorithm-based estimation process to generate simple 
    deterministic approximations that explain most of the structure of complex 
    stochastic processes. We have applied the software to empirical data, and 
    demonstrated it's ability to recover known data-generating processes by 
    simulating data with agent-based models and correctly deriving the 
    underlying decision models for multiple agent models and degrees of
    stochasticity.
	"""
	
	homepage = "https://jonathan-g.github.io/datafsm/"
	cran = "datafsm" 

	version("0.2.4", md5="6104a6ccef05b365f165c0fbd7055bdc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-caret@6:", type=("build", "run"))
	depends_on("r-ga@3.2:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))

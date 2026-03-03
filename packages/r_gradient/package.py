# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGradient(RPackage):
	"""Stochastic Quasi-Gradient Differential Evolution Optimization

	An optim-style implementation of the Stochastic Quasi-Gradient Differential Evolution (SQG-DE) optimization algorithm first published by Sala, Baldanzini, and Pierini (2018; <doi:10.1007/978-3-319-72926-8_27>). This optimization algorithm fuses the robustness of the population-based global optimization algorithm "Differential Evolution" with the efficiency of gradient-based optimization. The derivative-free algorithm uses population members to build stochastic gradient estimates, without any additional objective function evaluations. Sala, Baldanzini, and Pierini argue this algorithm is useful for 'difficult optimization problems under a tight function evaluation budget.' This package can run SQG-DE in parallel and sequentially.
	"""
	
	homepage = "https://github.com/bmgaldo/graDiEnt"
	cran = "graDiEnt" 

	version("1.0.1", md5="75757c3a46163f85406e353a76cdfc04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))

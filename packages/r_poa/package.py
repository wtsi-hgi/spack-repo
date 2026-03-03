# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoa(RPackage):
	"""Finds the Price of Anarchy for Routing Games

	Computes the optimal flow, Nash flow and the Price of Anarchy for any routing game defined within the game theoretical framework. The input is a routing game in the form of it’s cost and flow functions. Then transforms this into an optimisation problem, allowing both Nash and Optimal flows to be solved by nonlinear optimisation. See <https://en.wikipedia.org/wiki/Congestion_game> and Knight and Harper (2013) <doi:10.1016/j.ejor.2013.04.003> for more information.
	"""
	
	cran = "PoA" 

	version("1.2.1", md5="5dc9da51f0ce6ee3c2cafbabf8f11532")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))

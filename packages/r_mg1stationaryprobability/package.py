# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMg1stationaryprobability(RPackage):
	"""Computes Stationary Distribution for M/G/1 Queuing System

	The idea of a computational algorithm described in the article by Andronov M. et al. (2022) <https://link.springer.com/chapter/10.1007/978-3-030-92507-9_13>.
    The purpose of this package is to automate computations for a Markov-Modulated M/G/1 queuing system with alternating Poisson flow of arrivals. It offers a set of functions to calculate various mean indices of the system, including mean flow intensity, mean service busy and idle times, and the system's stationary probability.
	"""
	
	homepage = "https://github.com/MashroomMole/MG1StationaryProbability"
	cran = "MG1StationaryProbability" 

	version("0.1.2", md5="ebdfc7bb845bd9edb796652bf0cc2449")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-memoise@2.0.1:", type=("build", "run"))

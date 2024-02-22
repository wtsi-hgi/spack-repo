# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunexp(RPackage):
	"""Softball Run Expectancy using Markov Chains and Simulation

	Implements two methods of estimating runs scored in a softball 
    scenario: (1) theoretical expectation using discrete Markov chains and (2) empirical
    distribution using multinomial random simulation.  Scores are based on player-specific input 
    probabilities (out, single, double, triple, walk, and homerun).  Optional inputs include probability
    of attempting a steal, probability of succeeding in an attempted steal, and an indicator of whether
    a player is "fast" (e.g. the player could stretch home).  These probabilities may be 
    calculated from common player statistics that are publicly available on team's webpages. 
    Scores are evaluated based on a nine-player lineup and may be used to compare lineups, 
    evaluate base scenarios, and compare the offensive potential of individual players.  
    Manuscript forthcoming.  See Bukiet & Harold (1997) <doi:10.1287/opre.45.1.14> for 
    implementation of discrete Markov chains. 
	"""
	
	cran = "runexp" 

	version("0.2.1", md5="33de9880dbd408229b0ed5a7dfb568e8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))

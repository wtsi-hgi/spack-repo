# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtmcpack(RPackage):
	"""Suite of Functions Related to Discrete-Time Discrete-State
Markov Chains

	A series of functions which aid in both simulating and determining the properties of finite, discrete-time, discrete state markov chains.  Two functions (DTMC, MultDTMC) produce n iterations of a Markov Chain(s)  based on transition probabilities and an initial distribution.  The function FPTime determines the first passage time into each state.  The function statdistr determines the stationary distribution of a Markov Chain.
	"""
	
	cran = "DTMCPack" 

	version("0.1-3", md5="af876b4d1016270f74578a897f93c3fc")


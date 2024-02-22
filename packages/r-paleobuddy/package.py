# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaleobuddy(RPackage):
	"""Simulating Diversification Dynamics

	Simulation of species diversification, fossil records, and phylogenies. While the literature on species birth-death simulators is extensive, including important software like 'paleotree' and 'APE', we concluded there were interesting gaps to be filled regarding possible diversification scenarios. Here we strove for flexibility over focus, implementing a large array of regimens for users to experiment with and combine. In this way, 'paleobuddy' can be used in complement to other simulators as a flexible jack of all trades, or, in the case of scenarios implemented only here, can allow for robust and easy simulations for novel situations. Environmental data modified from that in 'RPANDA': Morlon H. et al (2016) <doi:10.1111/2041-210X.12526>.
	"""
	
	homepage = "https://github.com/brpetrucci/paleobuddy"
	cran = "paleobuddy" 

	version("1.0.0", md5="4320c49a02933965e95e052d8e7c1ed3")


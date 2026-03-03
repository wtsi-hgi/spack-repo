# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWildpoker(RPackage):
	"""Best Hand Analysis for Poker Variants Including Wildcards

	Provides insight into how the best hand for a poker game changes based on the game dealt, players who stay in until the showdown and wildcards added to the base game.  At this time the package does not support player tactics, so draw poker variants are not included.
	"""
	
	cran = "wildpoker" 

	version("1.1", md5="61eb0d3a4d25503ee3cf1fe1dbd2236b")

	depends_on("r@3.2:", type=("build", "run"))

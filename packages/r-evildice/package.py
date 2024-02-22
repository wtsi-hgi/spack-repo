# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvildice(RPackage):
	"""Test Dice Sets for Intransitive Properties

	Checks to see whether a supplied set of dice (their face values) are transitive, returning pair-win and group-roll win probabilities. Expected returns (mean magnitude of win/loss) are presented as well. 
	"""
	
	cran = "evilDice" 

	version("1.0", md5="4767f01438a12e85adf97386a42e4982")


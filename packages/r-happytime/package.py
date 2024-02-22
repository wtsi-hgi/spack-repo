# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHappytime(RPackage):
	"""Two Games to Relieve the Boredom

	There are two interesting games in this package, one is 2048 games(for windows), using up and down to control the direction until there is a 2048 figure. And the other is 'what to eat today',preparing for people who choose difficulties, including most of the delicious Cantonese cuisine.
	"""
	
	cran = "happytime" 

	version("0.1.0", md5="d99b40cca068c300e8d934fa433ff14a")


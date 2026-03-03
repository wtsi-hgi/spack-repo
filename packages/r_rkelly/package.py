# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkelly(RPackage):
	"""Translate Odds and Probabilities

	Calculates the Kelly criterion (Kelly, J.L. (1956) <doi:10.1002/j.1538-7305.1956.tb03809.x>) for bets given quoted prices, model predictions and commissions.
    Additionally it contains helper functions to calculate the probabilities for wins and draws in multi-leg games.
	"""
	
	cran = "RKelly" 

	version("1.0", md5="53e3bc16e14a22780b148b7620c98e65")


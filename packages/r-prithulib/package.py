# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrithulib(RPackage):
	"""Perform Random Experiments

	Enables user to perform the following:
    1. Roll 'n' number of die/dice (roll()).
    2. Toss 'n' number of coin(s) (toss()).
    3. Play the game of Rock, Paper, Scissors.
    4. Choose 'n' number of card(s) from a pack of 52 playing cards (Joker optional).
	"""
	
	cran = "prithulib" 

	version("1.0.2", md5="62087827bc7e7e641d546cd750a9fde0")


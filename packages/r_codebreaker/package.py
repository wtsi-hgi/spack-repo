# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodebreaker(RPackage):
	"""Retro Logic Game

	Logic game in the style of the early 1980s home computers 
    that can be played in the R console. This game is inspired by 
    Mastermind, a game that became popular in the 1970s.
    Can you break the code?
	"""
	
	homepage = "https://github.com/rolkra/codebreaker"
	cran = "codebreaker" 

	version("1.0.1", md5="f844cd60dd4ab910e482fc40b3f8b04b")

	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))

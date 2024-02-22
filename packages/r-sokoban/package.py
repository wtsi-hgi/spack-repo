# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSokoban(RPackage):
	"""Sokoban Game

	Interactively play a game of sokoban ,which has nine game levels.Sokoban is a type of transport puzzle, in which the player pushes boxes or crates around in a warehouse, trying to get them to storage locations.
	"""
	
	cran = "sokoban" 

	version("0.1.0", md5="40b6952bf375ffe16c512534a60a42f6")


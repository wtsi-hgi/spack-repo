# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlayerratings(RPackage):
	"""Dynamic Updating Methods for Player Ratings Estimation

	Implements schemes for estimating player or 
  team skill based on dynamic updating. Implemented methods include 
  Elo, Glicko, Glicko-2 and Stephenson. Contains pdf documentation 
  of a reproducible analysis using approximately two million chess 
  matches. Also contains an Elo based method for multi-player games
  where the result is a placing or a score. This includes zero-sum
  games such as poker and mahjong.
	"""
	
	cran = "PlayerRatings" 

	version("1.1-0", md5="5f70565a811a092c1c3520d4ccfd652a")

	depends_on("r@3.5:", type=("build", "run"))

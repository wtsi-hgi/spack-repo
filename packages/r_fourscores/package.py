# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFourscores(RPackage):
	"""A Game for Human vs. Human or Human vs. AI

	A game for two players: Who gets first four in a row (horizontal, vertical or diagonal) wins. As board game published by Milton Bradley, designed by Howard Wexler and Ned Strongin.
	"""
	
	cran = "FourScores" 

	version("1.5.1", md5="54cace9440ddc6c95671d9192bcd331e")

	depends_on("r@3:", type=("build", "run"))

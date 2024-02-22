# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnake(RPackage):
	"""Game of Snake

	Implements snake in R as a programming example, see <https://en.wikipedia.org/wiki/Snake_(video_game_genre)>.
	"""
	
	cran = "Snake" 

	version("1.0", md5="4b9ce2412c3017f2d1741b0e08ffd8b2")

	depends_on("r@3.5:", type=("build", "run"))

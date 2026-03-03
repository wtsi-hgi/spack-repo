# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPixelpuzzle(RPackage):
	"""Puzzle Game for the R Console

	Puzzle game that can be played in the R console.
  Restore the pixel art by shifting rows.
	"""
	
	homepage = "https://github.com/rolkra/pixelpuzzle"
	cran = "pixelpuzzle" 

	version("1.0.1", md5="88e18c3c8ae67b329f5afb29de852fde")

	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

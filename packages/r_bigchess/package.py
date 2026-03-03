# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigchess(RPackage):
	"""Read, Write, Manipulate, Explore Chess PGN Files and R API to
UCI Chess Engines

	Provides functions for reading *.PGN files with more than one game, including large files without copying it into RAM (using 'ff' package or 'RSQLite' package). Handle chess data and chess aggregated data, count figure moves statistics, create player profile, plot winning chances, browse openings. Set of functions of R API to communicate with UCI-protocol based chess engines.
	"""
	
	cran = "bigchess" 

	version("1.9.1", md5="4366d676dba5f1cb63595488a2554ce0")

	depends_on("r-processx", type=("build", "run"))

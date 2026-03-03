# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSudokualt(RPackage):
	"""Tools for Making and Spoiling Sudoku Games

	Tools for making, retrieving, displaying and solving sudoku games.
    This package is an alternative to the earlier sudoku-solver package,
    'sudoku'.  The present package uses a slightly different algorithm, has a
    simpler coding and presents a few more sugar tools, such as plot and print
    methods.  Solved sudoku games are of some interest in Experimental Design
    as examples of Latin Square designs with additional balance constraints.
	"""
	
	cran = "sudokuAlt" 

	version("0.2-1", md5="4dce29d52b953f19f78282285e0b763f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

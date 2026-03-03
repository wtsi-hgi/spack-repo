# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSudoku(RPackage):
	"""Sudoku Puzzle Generator and Solver

	Generates, plays, and solves Sudoku puzzles.  The GUI
        playSudoku() needs package "tkrplot" if you are not on Windows.
	"""
	
	cran = "sudoku" 

	version("2.8", md5="088ce39cfd1d78688ffa733c06df58e1")


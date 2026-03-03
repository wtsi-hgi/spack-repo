# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsdk(RPackage):
	"""Sudoku with R

	This is a sudoku game package with a shiny application for playing .
	"""
	
	cran = "RSDK" 

	version("1.0.1", md5="34cf0c3a127590deadae54653e6891e2")

	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-keys", type=("build", "run"))

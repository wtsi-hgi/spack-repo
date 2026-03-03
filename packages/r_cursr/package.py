# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCursr(RPackage):
	"""Cursor and Terminal Manipulation

	A toolbox for developing applications, games, simulations, or
    agent-based models in the R terminal. Included functions allow users to move the 
    cursor around the terminal screen, change text colors and attributes, clear the
    screen, hide and show the cursor, map key presses to functions, draw shapes and curves,
    among others. Most functionalities require users to be in a terminal (not the R GUI).
	"""
	
	cran = "cursr" 

	version("0.1.0", md5="99a83fcf80795cf0da9448ee54605789")

	depends_on("r-keypress", type=("build", "run"))

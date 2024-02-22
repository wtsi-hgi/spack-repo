# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazing(RPackage):
	"""Utilities for Making and Plotting Mazes

	Functionality for generating and plotting random mazes. The mazes are based on matrices, so can only consist of vertical and horizontal lines along a regular grid. But there is no need to use every possible space, so they can take on many different shapes.
	"""
	
	cran = "mazing" 

	version("1.0.5", md5="d68ce4dfea138f76ee7f49d2b05aa659")

	depends_on("r@4:", type=("build", "run"))

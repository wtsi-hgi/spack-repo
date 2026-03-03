# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerspectev(RPackage):
	"""Permutation of Species During Turnover Events

	Provides a robust framework for analyzing the extent to which differential survival with respect to higher level trait variation is reducible to lower level variation. In addition to its primary test, it also provides functions for simulation-based power analysis, reading in common data set formats, and visualizing results. Temporarily contains an edited version of function hr.mcp() from package 'wild1', written by Glen Sargeant. For tutorial see: http://evolve.zoo.ox.ac.uk/Evolve/Perspectev.html.
	"""
	
	cran = "perspectev" 

	version("1.1", md5="942a32d7b9b7160bec1b9ca007fe3213")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))

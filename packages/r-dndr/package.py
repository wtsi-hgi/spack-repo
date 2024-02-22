# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDndr(RPackage):
	"""Dungeons & Dragons Functions for Players and Dungeon Masters

	The goal of 'dndR' is to provide a suite of Dungeons & Dragons related functions.
    This package is meant to be useful both to players and Dungeon Masters (DMs).
    All functions currently focus on Fifth Edition (a.k.a. "5e") but once the next edition is published functions will likely be expanded to include any rule changes.
	"""
	
	cran = "dndR" 

	version("1.3.1", md5="7ee74b44a9fe479801080e9b75826200")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

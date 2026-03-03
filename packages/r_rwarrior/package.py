# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwarrior(RPackage):
	"""R Warrior - An AI Programming Game

	A port of Ruby Warrior.
    Teaches R programming in a fun and interactive way.
	"""
	
	cran = "rwarrior" 

	version("0.4.1", md5="6aff573e0bd24c3d4ca1b79af1a8d63c")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

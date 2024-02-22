# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazysql(RPackage):
	"""Lazy SQL Programming

	
    Helper functions to build SQL statements
    for dbGetQuery or dbSendQuery under program control.
    They are intended to increase speed of coding and
    to reduce coding errors. Arguments are carefully checked,
    in particular SQL identifiers such as names of tables or columns.
    More patterns will be added as required.
	"""
	
	homepage = "https://github.com/UweBlock/lazysql"
	cran = "lazysql" 

	version("0.1.3", md5="64a084fb9266ab75f42d56301b48c781")

	depends_on("r-checkmate@1.7.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

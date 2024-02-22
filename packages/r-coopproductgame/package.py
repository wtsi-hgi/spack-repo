# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoopproductgame(RPackage):
	"""Cooperative Aspects of Linear Production Programming Problems

	Computes cooperative games and allocation rules associated with linear production programming problems.
	"""
	
	cran = "coopProductGame" 

	version("2.0", md5="f689cf5ef3e31efc1f016b01112404a2")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-lpsolveapi@5.5.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-gametheory@2.7:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-kappalab", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))

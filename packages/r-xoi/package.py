# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXoi(RPackage):
	"""Tools for Analyzing Crossover Interference

	Analysis of crossover interference in experimental crosses,
    particularly regarding the gamma model. See, for example,
    Broman and Weber (2000) <doi:10.1086/302923>.
	"""
	
	homepage = "https://github.com/kbroman/xoi"
	cran = "xoi" 

	version("0.72", md5="7d6f9fb505b325ee162fcf5c95b5b43d")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBillboard(RPackage):
	"""Contains Data of Billboard Hot 100 Songs

	Contains data sets regarding songs on the Billboard Hot 100 list
    from 1960 to 2016. The data sets include the ranks for the given year,
    musical features of a lot of the songs and lyrics for several of the songs
    as well.
	"""
	
	homepage = "https://github.com/mikkelkrogsholm/billboard"
	cran = "billboard" 

	version("0.1.0", md5="30973197dfe98a950ed6b86389fe08cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

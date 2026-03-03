# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlr(RPackage):
	"""Semi-Latin Rectangles

	A facility to generate balanced semi-Latin rectangles with any cell size (preferably up to ten) with given number of treatments, see Uto, N.P. and Bailey, R.A. (2020). "Balanced Semi-Latin rectangles: properties, existence and constructions for block size two". Journal of Statistical Theory and Practice, 14(3), 1-11, <doi:10.1007/s42519-020-00118-3>. It also provides facility to generate partially balanced semi-Latin rectangles for cell size 2, 3 and 4 for any number of treatments.
	"""
	
	cran = "slr" 

	version("1.3.0", md5="b9912070d4c8823fc7ef939fa7f3b254")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ibd", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))

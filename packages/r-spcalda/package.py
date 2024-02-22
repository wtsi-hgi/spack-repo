# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcalda(RPackage):
	"""A New Reduced-Rank Linear Discriminant Analysis Method

	A new reduced-rank LDA method which works for high dimensional multi-class data. 
	"""
	
	cran = "SPCALDA" 

	version("1.0", md5="724c77bc358ea123a5d9ffb90c09089a")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

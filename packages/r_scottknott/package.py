# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScottknott(RPackage):
	"""The ScottKnott Clustering Algorithm

	Perform the balanced (Scott and Knott, 1974) and unbalanced <doi:10.1590/1984-70332017v17n1a1> Scott & Knott algorithm.
	"""
	
	homepage = "https://github.com/ivanalaman/ScottKnott"
	cran = "ScottKnott" 

	version("1.3-2", md5="139e5c5f7523a5f03d20cf9ad500d1a3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))

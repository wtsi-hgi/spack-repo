# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDietr(RPackage):
	"""Diet Estimated Trophic Levels

	Estimates fractional trophic level from quantitative and qualitative diet data and calculates electivity indices in R. Borstein (2020) <doi:10.1007/s10750-020-04417-5>.
	"""
	
	homepage = "https://github.com/sborstein/dietr"
	cran = "dietr" 

	version("1.1.4", md5="0c329b193c31a9ae36270ec3ceaa37b9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rfishbase@4.1:", type=("build", "run"))

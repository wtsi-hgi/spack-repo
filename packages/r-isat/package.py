# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsat(RPackage):
	"""Extract Cell Density and Nearest Distance Based on 'PerkinElmer
InForm' Software Output

	Reads the output of the 'PerkinElmer InForm' software <http://www.perkinelmer.com/product/inform-cell-analysis-one-seat-cls135781>. In addition to cell-density count, it can derive statistics of intercellular spatial distance for each cell-type.
	"""
	
	cran = "ISAT" 

	version("1.0.5", md5="b84ed9b2fa3b1043fd3379b7284e311c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

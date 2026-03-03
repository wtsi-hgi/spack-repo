# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoranking(RPackage):
	"""Co-Ranking Matrix

	Calculates the co-ranking matrix to assess the
    quality of a dimensionality reduction.
	"""
	
	homepage = "https://www.guido-kraemer.com/software/coranking/"
	cran = "coRanking" 

	version("0.2.4", md5="73f07ed26db31ef7d0e67f4174de1b66")


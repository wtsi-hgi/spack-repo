# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiagonals(RPackage):
	"""Block Diagonal Extraction or Replacement

	Several tools for handling block-matrix diagonals and similar
    constructs are implemented. Block-diagonal matrices can be extracted or removed
    using two small functions implemented here. In addition, non-square matrices
    are supported. Block diagonal matrices occur when two dimensions of a data set
    are combined along one edge of a matrix. For example, trade-flow data in the
    'decompr' and 'gvc' packages have each country-industry combination occur along
    both edges of the matrix.
	"""
	
	homepage = "https://qua.st/diagonals"
	cran = "diagonals" 

	version("6.4.0", md5="a317f663faf5727792901ab9c9abd272")

	depends_on("r@2.10:", type=("build", "run"))

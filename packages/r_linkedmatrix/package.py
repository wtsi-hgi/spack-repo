# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkedmatrix(RPackage):
	"""Column-Linked and Row-Linked Matrices

	A class that links matrix-like objects (nodes) by rows or by
    columns while behaving similarly to a base R matrix. Very large matrices
    are supported if the nodes are file-backed matrices.
	"""
	
	homepage = "https://github.com/QuantGen/LinkedMatrix"
	cran = "LinkedMatrix" 

	version("1.4.0", md5="aee2086615a51fa4c82b23c4aaa61526")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-crochet@2.3:", type=("build", "run"))

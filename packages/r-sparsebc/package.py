# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsebc(RPackage):
	"""Sparse Biclustering of Transposable Data

	Implements the sparse biclustering proposal of Tan and Witten (2014), Sparse biclustering of transposable data. Journal of Computational and Graphical Statistics  23(4):985-1008.
	"""
	
	cran = "sparseBC" 

	version("1.2", md5="5f291e836f0a238f4697b2c40971f42e")

	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))

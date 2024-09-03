# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RQlcmatrix(RPackage):
	"""Utility Sparse Matrix Functions for Quantitative Language
Comparison

	Extension of the functionality of the Matrix package for using sparse matrices. Some of the functions are very general, while other are highly specific for special data format as used for quantitative language comparison (QLC).
	"""
	
	cran = "qlcMatrix" 

	version("0.9.7", md5="3b0734cb96c9cae62f760de1d4a4a8a7")

	depends_on("r-matrix@1.1.0:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-slam@0.1-32:", type=("build", "run"))
	depends_on("r-sparsesvd", type=("build", "run"))
	depends_on("r-docopt", type=("build", "run"))

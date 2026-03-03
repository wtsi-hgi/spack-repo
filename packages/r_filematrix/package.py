# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilematrix(RPackage):
	"""File-Backed Matrix Class with Convenient Read and Write Access

	Interface for working with large matrices stored in files,
        not in computer memory. Supports multiple non-character
        data types (double, integer, logical and raw) of
        various sizes (e.g. 8 and 4 byte real values).
        Access to parts of the matrix is done by indexing, 
        exactly as with usual R matrices.
        Supports very large matrices.
        Tested on multi-terabyte matrices.
        Allows for more than 2^32 rows or columns.
        Allows for quick addition of extra columns to a filematrix.
        Cross-platform as the package has R code only.
	"""
	
	homepage = "https://github.com/andreyshabalin/filematrix"
	cran = "filematrix" 

	version("1.3", md5="cfa4f4793c89ea6d8d4a09792e9ca2fa")


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmatrix(RPackage):
	"""Read from/Write to Disk Matrices with any Data Type in a Binary
Format

	A mainly instrumental package meant to allow other packages whose core is written in 'C++' to read, write
        and manipulate matrices in a binary format so that the memory used for them is no more than strictly needed. Its functionality
        is already inside 'parallelpam' and 'scellpam', so if you have installed any of these, you do not need to install 'jmatrix'.
        Using just the needed memory is not always true with 'R' matrices or vectors, since by default they are of double type. Trials
        like the 'float' package have been done, but to use them you have to coerce a matrix already loaded in 'R' memory to a float matrix,
        and then you can delete it. The problem comes when your computer has not memory enough to hold the matrix in the first place, so
        you are forced to load it by chunks. This is the problem this package tries to address (with partial success, but this is a
        difficult problem since 'R' is not a strictly typed language, which is anyway quite hard to get in an interpreted language).
	This package allows the creation and manipulation of full, sparse and symmetric matrices of any standard data type.
	"""
	
	cran = "jmatrix" 

	version("1.5", md5="030b5380be143167ea8eada67ff109fa")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-memuse@4.2.1:", type=("build", "run"))

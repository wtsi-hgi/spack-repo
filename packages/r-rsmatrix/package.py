# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsmatrix(RPackage):
	"""Matrices for Repeat-Sales Price Indexes

	Calculate the matrices in
    Shiller (1991, <doi:10.1016/S1051-1377(05)80028-2>) that serve as the
    foundation for many repeat-sales price indexes.
	"""
	
	homepage = "https://marberts.github.io/rsmatrix/"
	cran = "rsmatrix" 

	version("0.2.8", md5="9ae47c58ef09d99ae842408830e129cc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))

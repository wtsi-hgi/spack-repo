# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymdmatrix(RPackage):
	"""Partitioned Symmetric Matrices

	A matrix-like class to represent a symmetric matrix partitioned
    into file-backed blocks.
	"""
	
	homepage = "https://github.com/QuantGen/symDMatrix"
	cran = "symDMatrix" 

	version("2.1.1", md5="03febf700d0a17fcf2eeaf68a23e8596")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-linkedmatrix@1.3:", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-bit", type=("build", "run"))

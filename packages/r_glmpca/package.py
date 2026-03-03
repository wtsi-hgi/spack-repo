# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmpca(RPackage):
	"""Dimension Reduction of Non-Normally Distributed Data

	Implements a generalized version of principal components analysis
    (GLM-PCA) for dimension reduction of non-normally distributed data such as
    counts or binary matrices.
    Townes FW, Hicks SC, Aryee MJ, Irizarry RA (2019) <doi:10.1186/s13059-019-1861-6>.
    Townes FW (2019) <arXiv:1907.02647>.
	"""
	
	homepage = "https://github.com/willtownes/glmpca"
	cran = "glmpca" 

	version("0.2.0", md5="66fdfc9cea90e82dadd1d47703ff50d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

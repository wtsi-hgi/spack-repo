# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterleave(RPackage):
	"""Converts Tabular Data to Interleaved Vectors

	Converts matrices and lists of matrices into a single vector by interleaving 
    their values. That is, each element of the result vector is filled from the input 
    matrices one row at a time. This is the same as transposing a matrix, then removing the 
    dimension attribute, but is designed to operate on matrices in nested list structures.
	"""
	
	cran = "interleave" 

	version("0.1.2", md5="ce6aed8589817f5adacdd42305c73715")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-geometries@0.2.4:", type=("build", "run"))

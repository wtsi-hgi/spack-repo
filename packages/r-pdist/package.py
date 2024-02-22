# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdist(RPackage):
	"""Partitioned Distance Function

	Computes the euclidean distance between rows of a matrix X
        and rows of another matrix Y.  Previously, this could be done
        by binding the two matrices together and calling 'dist', but
        this creates unnecessary computation by computing the distances
        between a row of X and another row of X, and likewise for Y.
        pdist strictly computes distances across the two matrices, not
        within the same matrix, making computations significantly
        faster for certain use cases.
	"""
	
	homepage = "https://github.com/jeffwong/pdist"
	cran = "pdist" 

	version("1.2.1", md5="f6bd156a9a05bc3b615ce8fc27a78e4d")


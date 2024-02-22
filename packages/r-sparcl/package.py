# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparcl(RPackage):
	"""Perform Sparse Hierarchical Clustering and Sparse K-Means
Clustering

	Implements the sparse clustering methods of Witten and
        Tibshirani (2010): "A framework for feature selection in
        clustering"; published in Journal of the American Statistical
        Association 105(490): 713-726.
	"""
	
	cran = "sparcl" 

	version("1.0.4", md5="123fb53fed12e4de49926be67c61afc0")


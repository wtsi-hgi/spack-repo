# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorbin(RPackage):
	"""Generate High-Dimensional Binary Data with Correlation
Structures

	We design algorithms with linear time complexity with respect to the dimension for three commonly studied correlation structures, including exchangeable, decaying-product and K-dependent correlation structures, and extend the algorithms to generate binary data of general non-negative correlation matrices with quadratic time complexity. Jiang, W., Song, S.,  Hou, L. and Zhao, H. "A set of efficient methods to generate high-dimensional binary data with specified correlation structures." The American Statistician. See <doi:10.1080/00031305.2020.1816213> for a detailed presentation of the method.
	"""
	
	cran = "CorBin" 

	version("1.0.0", md5="91150d4d5e81f9fb31fc3ac9d82f611c")


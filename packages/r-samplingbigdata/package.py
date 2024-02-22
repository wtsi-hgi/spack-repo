# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingbigdata(RPackage):
	"""Sampling Methods for Big Data

	Select sampling methods for probability samples using large data sets.  This includes spatially balanced sampling in multi-dimensional spaces with any prescribed inclusion probabilities. All implementations are written in C with efficient data structures such as k-d trees that easily scale to several million rows on a modern desktop computer. 
	"""
	
	homepage = "https://github.com/jlisic/SamplingBigData"
	cran = "SamplingBigData" 

	version("1.0.0", md5="1e4d5950613d6023a0c9e9116f027ef0")


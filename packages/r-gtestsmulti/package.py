# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtestsmulti(RPackage):
	"""New Graph-Based Multi-Sample Tests

	New multi-sample tests for testing whether multiple samples are from the same distribution. They work well particularly for high-dimensional data.
    Song, H. and Chen, H. (2022) 
    <arXiv:2205.13787>.
	"""
	
	cran = "gTestsMulti" 

	version("0.1.1", md5="07b7ec682a07576bcf0f9b7f94cb7496")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

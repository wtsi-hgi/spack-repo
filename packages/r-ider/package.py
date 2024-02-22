# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIder(RPackage):
	"""Various Methods for Estimating Intrinsic Dimension

	An implementation of various methods for estimating intrinsic
    dimension of vector-valued dataset or distance matrix. Most methods implemented
    are based on different notion of fractal dimension such as the capacity
    dimension, the box-counting dimension, and the information dimension.
	"""
	
	cran = "ider" 

	version("0.1.1", md5="a08893e8a13a18e1e4e6453e30e23e3b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGstream(RPackage):
	"""Graph-Based Sequential Change-Point Detection for Streaming Data

	Uses an approach based on k-nearest neighbor information to sequentially detect change-points. Offers analytic approximations for false discovery control given user-specified average run length.  Can be applied to any type of data (high-dimensional, non-Euclidean, etc.) as long as a reasonable similarity measure is available.  See references (1) Chen, H. (2019) Sequential change-point detection based on nearest neighbors. The Annals of Statistics, 47(3):1381-1407. (2) Chu, L. and Chen, H. (2018) Sequential change-point detection for high-dimensional and non-Euclidean data <arXiv:1810.05973>. 
	"""
	
	cran = "gStream" 

	version("0.2.0", md5="ab7a4bc40e430bf835cb2afd1812f83a")

	depends_on("r@3.0.1:", type=("build", "run"))

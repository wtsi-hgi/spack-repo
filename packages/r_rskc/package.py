# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRskc(RPackage):
	"""Robust Sparse K-Means

	This RSKC package contains a function RSKC which runs the robust sparse K-means clustering algorithm.
	"""
	
	cran = "RSKC" 

	version("2.4.2", md5="5eb06b076dd9dfefb4d5a214b24a60e4")

	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r@2.14:", type=("build", "run"))

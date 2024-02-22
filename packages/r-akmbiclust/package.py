# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAkmbiclust(RPackage):
	"""Alternating K-Means Biclustering

	Implements the alternating k-means biclustering algorithm in Fraiman and Li (2020) <arXiv:2009.04550>.
	"""
	
	cran = "akmbiclust" 

	version("0.1.0", md5="f4d2395f8f433f0b8ca54c31f367e491")

	depends_on("r@2.10:", type=("build", "run"))

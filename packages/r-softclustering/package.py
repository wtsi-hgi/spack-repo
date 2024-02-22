# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoftclustering(RPackage):
	"""Soft Clustering Algorithms

	It contains soft clustering algorithms, in particular approaches derived from rough set theory: Lingras & West original rough k-means, Peters' refined rough k-means, and PI rough k-means. It also contains classic k-means and a corresponding illustrative demo.
	"""
	
	cran = "SoftClustering" 

	version("2.1.3", md5="457b79cea1cd3597838ab6e3e9950973")

	depends_on("r@4.1:", type=("build", "run"))

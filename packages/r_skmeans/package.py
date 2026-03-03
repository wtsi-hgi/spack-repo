# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkmeans(RPackage):
	"""Spherical k-Means Clustering

	Algorithms to compute spherical k-means partitions.
  Features several methods, including a genetic and a fixed-point
  algorithm and an interface to the CLUTO vcluster program.
	"""
	
	cran = "skmeans" 

	version("0.2-16", md5="872d5851fd972dde7671b3fe099dbbaf")

	depends_on("r-slam@0.1.31:", type=("build", "run"))
	depends_on("r-clue@0.3.39:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))

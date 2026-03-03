# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCclust(RPackage):
	"""Convex Clustering Methods and Clustering Indexes

	Convex Clustering methods, including K-means algorithm,
  On-line Update algorithm (Hard Competitive Learning) and Neural Gas
  algorithm (Soft Competitive Learning), and calculation of several
  indexes for finding the number of clusters in a data set.
	"""
	
	cran = "cclust" 

	version("0.6-26", md5="ab2ad23ceee7992d32cb5c88cc7b14ab")


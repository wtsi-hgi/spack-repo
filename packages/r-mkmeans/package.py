# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkmeans(RPackage):
	"""A Modern K-Means (MKMeans) Clustering Algorithm

	It's a Modern K-Means clustering algorithm allowing data of any number of dimensions, any initial center, and any number of clusters to expect.
	"""
	
	cran = "MKMeans" 

	version("2.1", md5="86a1b5964319f4c41740c84a2b00ff75")


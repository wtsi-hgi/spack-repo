# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrclus(RPackage):
	"""Subspace Clustering Based on Arbitrarily Oriented Projected
Cluster Generation

	Functions to perform subspace clustering and classification. 
	"""
	
	cran = "orclus" 

	version("0.2-6", md5="7d9fba1a90dad56f151a5f2d7bf30c05")


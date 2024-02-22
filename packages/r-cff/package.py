# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCff(RPackage):
	"""Simple Similarity for User-Based Collaborative Filtering Systems

	A simple, fast algorithm to find the neighbors and similarities of users in user-based filtering systems,
             to break free from the complex computation of existing similarity formulas and the ability to solve big data.
	"""
	
	cran = "CFF" 

	version("1.0", md5="ad39ee6ae872993f2cf7b91fae8e50a5")


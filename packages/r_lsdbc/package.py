# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsdbc(RPackage):
	"""Locally Scaled Density Based Clustering

	Implementation of Locally Scaled Density Based Clustering (LSDBC) algorithm proposed by Bicici and Yuret (2007) <doi:10.1007/978-3-540-71618-1_82>. This package also contains some supporting functions such as betaCV() function and get_spectral() function.
	"""
	
	cran = "lsdbc" 

	version("0.1.0", md5="ce0a8515689cf06764546509b0f8e0fd")


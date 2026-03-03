# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKriging(RPackage):
	"""Ordinary Kriging

	An implementation of a simple and highly optimized ordinary kriging algorithm to plot geographical data.
	"""
	
	cran = "kriging" 

	version("1.2", md5="2ab6d7b85113ece6f21847a6d2968aac")


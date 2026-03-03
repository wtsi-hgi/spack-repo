# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransformmos(RPackage):
	"""Transform MOS Values to be Robust for using Rank Based
Statistics

	Implementation of the transformation of the Mean Opinion Scores (MOS) to be used before applying the rank based statistical techniques. The method and its necessity is described in: Babak Naderi, Sebastian Möller (2020) <arXiv:2004.11490>.
	"""
	
	cran = "transformmos" 

	version("0.1.0", md5="033def46adae341292d3095f021f5eaa")


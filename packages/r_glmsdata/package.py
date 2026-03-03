# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmsdata(RPackage):
	"""Generalized Linear Model Data Sets

	Data sets from the book Generalized Linear Models with Examples in R by Dunn and Smyth.
	"""
	
	cran = "GLMsData" 

	version("1.4", md5="169e65beb55e576eab79de4815f5412d")


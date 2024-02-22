# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridbezier(RPackage):
	"""Bezier Curves in 'grid'

	Functions for rendering Bezier
             curves (Pomax, 2018) <https://pomax.github.io/bezierinfo/>
             in 'grid'.  
             There is support for both quadratic and cubic Bezier curves.
             There are also functions for calculating points on curves,
             tangents to curves, and normals to curves.
	"""
	
	homepage = "https://github.com/pmur002/gridbezier"
	cran = "gridBezier" 

	version("1.1-1", md5="bac1bc7044f38d0fa7741d2420a2592d")


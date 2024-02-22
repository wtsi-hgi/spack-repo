# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaintmap(RPackage):
	"""Plotting Paintmaps

	Plots matrices of colours as grids of coloured squares - aka heatmaps, 
	guaranteeing legible row and column names, 
	without transformation of values, 
	without re-ordering rows or columns,
	and without dendrograms.
	"""
	
	cran = "paintmap" 

	version("1.0", md5="dfea07c16287fce1eca4d238b3b2a46e")


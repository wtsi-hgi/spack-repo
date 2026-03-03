# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotMatrix(RPackage):
	"""Visualizes a Matrix as Heatmap

	Visualizes a matrix object plainly as heatmap. It provides S3 functions to plot simple matrices and loading matrices.
	"""
	
	homepage = "https://github.com/sigbertklinke/plot.matrix"
	cran = "plot.matrix" 

	version("1.6.2", md5="27d432a2efba9fa9311436f28d9254ba")


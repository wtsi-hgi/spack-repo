# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContourfunctions(RPackage):
	"""Create Contour Plots from Data or a Function

	Provides functions for making contour plots.
  The contour plot can be created from grid data, a function,
  or a data set. If non-grid data is given, then a Gaussian
  process is fit to the data and used to create the contour plot.
	"""
	
	homepage = "https://github.com/CollinErickson/contour"
	cran = "ContourFunctions" 

	version("0.1.1", md5="84ad6c41335cded4eeb691b1abbecbe5")


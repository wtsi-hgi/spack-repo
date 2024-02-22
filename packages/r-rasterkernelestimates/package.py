# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterkernelestimates(RPackage):
	"""Kernel Based Estimates on in-Memory Raster Images

	Performs kernel based estimates on in-memory raster images 
  from the raster package.  These kernel estimates include local means
  variances, modes, and quantiles.  All results are in the form of 
  raster images, preserving original resolution and projection attributes.
	"""
	
	homepage = "http://meanmean.me/blog/rasterKernel/rasterKernel.html"
	cran = "rasterKernelEstimates" 

	version("1.0.2", md5="e46402881cde340eca18c117d3dd8d12")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))

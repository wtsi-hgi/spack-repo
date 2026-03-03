# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaussplotr(RPackage):
	"""Fit, Predict and Plot 2D Gaussians

	
    Functions to fit two-dimensional Gaussian functions, predict values from
    fits, and produce plots of predicted data via either 'ggplot2' or base R 
    plotting.
	"""
	
	homepage = "https://github.com/vbaliga/gaussplotR"
	cran = "gaussplotR" 

	version("0.2.5", md5="6bdbfc3b29aa9394b186248ae0a08d5c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-metr@0.7:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))

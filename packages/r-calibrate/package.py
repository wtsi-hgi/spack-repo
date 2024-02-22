# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibrate(RPackage):
	"""Calibration of Scatterplot and Biplot Axes

	Package for drawing calibrated scales with tick marks on (non-orthogonal) 
             variable vectors in scatterplots and biplots. Also provides some functions for biplot creation and
	     for multivariate analysis such as principal coordinate analysis.
	"""
	
	cran = "calibrate" 

	version("1.7.7", md5="8b244af41c298c7bae178b6a58ee422d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasuring(RPackage):
	"""Detection and Control of Tree-Ring Widths on Scanned Image
Sections

	Identification of ring borders on scanned image sections from dendrochronological samples. Processing of image reflectances to produce gray matrices and time series of smoothed gray values. Luminance data is plotted on segmented images for users to perform both: visual identification of ring borders or control of automatic detection. Routines to visually include/exclude ring borders on the R graphical devices, or automatically detect ring borders using a linear detection algorithm. This algorithm detects ring borders according to positive/negative extreme values in the smoothed time-series of gray values. Most of the in-package routines can be recursively implemented using the multiDetect() function.
	"""
	
	cran = "measuRing" 

	version("0.5", md5="aecaec318a4f462719b2fef5c769b9e9")

	depends_on("r-pastecs", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmatools(RPackage):
	"""Data Management Tools for Real-Time Monitoring/Ecological
Momentary Assessment Data

	Do data management functions common in real-time monitoring (also called: ecological momentary assessment, experience sampling, micro-longitudinal) data, including creating power curves for multilevel data, centering on participant means and merging event-level data into momentary data sets where you need the events to correspond to the nearest data point in the momentary data. This is VERY early release software, and more features will be added over time. 
	"""
	
	cran = "EMAtools" 

	version("0.1.4", md5="2d52010419177296cd7dde02d8a158bd")

	depends_on("r-datacombine", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-sjstats@0.10.2:", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

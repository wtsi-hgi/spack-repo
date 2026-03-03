# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbubbles(RPackage):
	"""Mini Bubble Plots for Comparison of Discrete Data with 'ggplot2'

	When comparing discrete data mini bubble plots allow displaying 
   more information than traditional bubble plots via colour, shape or labels. 
   Exact overlapping coordinates will be transformed so they surround the
   original point circularly without overlapping. This is implemented as a 
   position_surround() function for 'ggplot2'.
	"""
	
	cran = "ggBubbles" 

	version("0.1.4", md5="02a8a19f678c217b10f333521fabb50c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

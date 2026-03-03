# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTframe(RPackage):
	"""Time Frame Coding Kernel

	A kernel of functions for programming 
	time series methods in a way that is relatively independently of the 
	representation of time. Also provides plotting, time windowing, 
	and some
	other utility functions which are specifically intended for time series.
	See the Guide distributed as a vignette, or ?tframe.Intro for more
	details. (User utilities are in package tfplot.)
	"""
	
	homepage = "http://tsanalysis.r-forge.r-project.org/"
	cran = "tframe" 

	version("2015.12-1.1", md5="d1c4b3aacce908f15aff5370714b3dd3")

	depends_on("r@2.5:", type=("build", "run"))

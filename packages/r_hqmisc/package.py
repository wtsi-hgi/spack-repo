# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHqmisc(RPackage):
	"""Miscellaneous Convenience Functions and Dataset

	Miscellaneous convenience functions and wrapper functions 
	to convert frequencies between Hz, semitones, mel and Bark, 
	to create a matrix of dummy columns from a factor, 
	to determine whether x lies in range [a,b], 
	and to add a bracketed line to an existing plot.
	This package also contains an example data set of a stratified sample
	of 80 talkers of Dutch. 
	"""
	
	cran = "hqmisc" 

	version("0.2-1", md5="6078fef2206ada370830742aa655737b")

	depends_on("r@3:", type=("build", "run"))

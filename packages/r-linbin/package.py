# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinbin(RPackage):
	"""Binning and Plotting of Linearly Referenced Data

	Short for 'linear binning', the linbin package provides functions
    for manipulating, binning, and plotting linearly referenced data. Although
    developed for data collected on river networks, it can be used with any interval
    or point data referenced to a 1-dimensional coordinate system. Flexible bin
    generation and batch processing makes it easy to compute and visualize variables
    at multiple scales, useful for identifying patterns within and between variables
    and investigating the influence of scale of observation on data interpretation.
	"""
	
	homepage = "https://github.com/ezwelty/linbin"
	cran = "linbin" 

	version("0.1.3", md5="3006735c8c1b533cc3aefa78a1ea4720")

	depends_on("r@3.0.1:", type=("build", "run"))

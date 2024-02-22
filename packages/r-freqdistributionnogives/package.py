# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqdistributionnogives(RPackage):
	"""Automated Cumulative Frequency Plots for Grouped Distribution

	Input has to be in the form of vectors of lower class limits and upper class limits and frequencies; the output will give a cumulative frequency distribution table with cumulative frequency plot.
	"""
	
	homepage = "https://github.com/Harshit-Budakoti/freqdistributionNogives"
	cran = "freqdistributionNogives" 

	version("0.1.1", md5="243d3bf5f8734a38ffd9a0ed3b03026e")


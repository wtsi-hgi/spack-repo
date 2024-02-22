# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqdist(RPackage):
	"""Frequency Distribution

	Generates a frequency distribution. The frequency
    distribution includes raw frequencies, percentages in each category, and
    cumulative frequencies. The frequency distribution can be stored as a data
    frame.
	"""
	
	cran = "freqdist" 

	version("0.1", md5="16350fe918c56f4b7f9d5434a18751d0")


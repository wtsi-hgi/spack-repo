# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptbin(RPackage):
	"""Optimal Binning of Data

	Defines thresholds for breaking data into a number of
  discrete levels, minimizing the (mean) squared error within all bins.
	"""
	
	cran = "optbin" 

	version("1.3", md5="8092a1d1759c66571e1ac7d91bbe119c")


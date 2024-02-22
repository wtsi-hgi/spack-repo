# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCusumdesign(RPackage):
	"""Compute Decision Interval and Average Run Length for CUSUM
Charts

	Computation of decision intervals (H) and average run lengths (ARL) for CUSUM charts. Details of the method are seen in Hawkins and Olwell (2012): Cumulative sum charts and charting for quality improvement, Springer Science & Business Media.
	"""
	
	cran = "CUSUMdesign" 

	version("1.1.5", md5="6612245adcdef5148fe1c545477d1ce5")


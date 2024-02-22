# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbest(RPackage):
	"""Detecting Breakpoints and Estimating Segments in Trend

	A program for analyzing vegetation time series, with two algorithms: 1) change detection algorithm that detects trend changes, determines their type (abrupt or non-abrupt), and estimates their timing, magnitude, number, and direction; 2) generalization algorithm that simplifies the temporal trend into main features. The user can set the number of major breakpoints or magnitude of greatest changes of interest for detection, and can control the generalization process by setting an additional parameter of generalization-percentage.
	"""
	
	cran = "DBEST" 

	version("1.8", md5="dc65f6a70a378483442324e1f17ff4f4")

	depends_on("r-zoo", type=("build", "run"))

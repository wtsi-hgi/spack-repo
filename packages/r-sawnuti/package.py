# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSawnuti(RPackage):
	"""Comparing Sequences with Non-Uniform Time Intervals

	The SAWNUTI algorithm performs sequence comparison for finite sequences of discrete events with non-uniform time intervals. Further description of the algorithm can be found in the paper: A. Murph, A. Flynt, B. R. King (2021). Comparing finite sequences of discrete events with non-uniform time intervals, Sequential Analysis, 40(3), 291-313. <doi:10.1080/07474946.2021.1940491>.
	"""
	
	cran = "sawnuti" 

	version("0.1.1", md5="eae75a1044805f12ec0819440267fe3a")


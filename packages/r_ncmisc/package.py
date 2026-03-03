# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcmisc(RPackage):
	"""Miscellaneous Functions for Creating Adaptive Functions and
Scripts

	A set of handy functions. Includes a versatile one line progress bar, one 
 line function timer with detailed output, time delay function, text histogram, object 
 preview, CRAN package search, simpler package installer, Linux command install check, 
 a flexible Mode function, top function, simulation of correlated data, and more.
	"""
	
	cran = "NCmisc" 

	version("1.2.0", md5="d3e09dcb38e0f2042a683d2c50b5da21")

	depends_on("r@3.10:", type=("build", "run"))

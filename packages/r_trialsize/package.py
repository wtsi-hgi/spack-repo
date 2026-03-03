# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrialsize(RPackage):
	"""R Functions for Chapter 3,4,6,7,9,10,11,12,14,15 of Sample Size
Calculation in Clinical Research

	Functions and Examples in Sample Size Calculation in
        Clinical Research.
	"""
	
	cran = "TrialSize" 

	version("1.4", md5="a8eb70718f9685ccda505bd9aa4b4b1d")


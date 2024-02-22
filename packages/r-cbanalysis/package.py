# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbanalysis(RPackage):
	"""Coffee Break Descriptive Analysis

	A set of functions that helps you to generate descriptive statistics based on the variable types.
	"""
	
	cran = "cbanalysis" 

	version("0.2.0", md5="39d4e5ef22f184713b622170dc13e80b")


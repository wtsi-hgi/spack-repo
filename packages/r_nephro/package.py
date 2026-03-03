# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNephro(RPackage):
	"""Utilities for Nephrology

	Set of functions to estimate kidney function and other phenotypes of interest in nephrology based on different biomechimal traits. 
	"""
	
	cran = "nephro" 

	version("1.4", md5="9988d55bddbadae6313cfd4cc5a50235")


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobalopttests(RPackage):
	"""Objective functions for benchmarking the performance of global
optimization algorithms

	This package makes available 50 objective functions for benchmarking the performance of global optimization algorithms 
	"""
	
	cran = "globalOptTests" 

	version("1.1", md5="f7218d7ddf655b22877b27878ddb0701")


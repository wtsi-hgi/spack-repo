# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtests(RPackage):
	"""Graph-Based Two-Sample Tests

	Four graph-based tests are provided for testing whether two samples are from the same distribution.  It works for both continuous data and discrete data.
	"""
	
	cran = "gTests" 

	version("0.2", md5="7e805cd248ff143b923b0a1d9fa96f2a")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))

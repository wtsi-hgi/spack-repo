# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwlaxeref(RPackage):
	"""Cross-References Lake Identifiers Between Different Data Sets

	Handy helper package for cross-referencing lake identifiers 
    among different data sets in the Midwestern United States. There are 
    multiple different state, regional, and federal agencies that have 
    different identifiers on lakes. This package helps you to go between them.
	"""
	
	cran = "mwlaxeref" 

	version("0.0.1", md5="abfae068969d33b321fa8dce76a7ec8c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))

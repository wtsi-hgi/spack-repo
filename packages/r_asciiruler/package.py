# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsciiruler(RPackage):
	"""Render an ASCII Ruler

	An ASCII ruler is for measuring text and is especially useful for sequence analysis. Included in this package are methods to create ASCII rulers and associated GenBank sequence blocks, multi-column text displays that make it easy for viewers to locate nucleotides by position.
	"""
	
	cran = "asciiruler" 

	version("0.2", md5="b140ed3a1cacf41b76ab87957358c950")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

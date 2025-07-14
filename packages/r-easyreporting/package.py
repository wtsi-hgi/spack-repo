# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyreporting(RPackage):
	"""Helps creating report for improving Reproducible Computational Research

	An S4 class for facilitating the automated creation of rmarkdown files inside other packages/software even without knowing rmarkdown language. Best if implemented in functions as "recursive" style programming.
	"""
	
	bioc = "easyreporting"

	version("1.20.0", commit="8660dd4aeac60e9fc7147bb4868e032a74927baf")
	version("1.14.0", commit="84e6e967b545366fc258d110222f7405aa03989d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

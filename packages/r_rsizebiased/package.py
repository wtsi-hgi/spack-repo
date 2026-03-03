# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsizebiased(RPackage):
	"""Hypothesis Testing Based on R-Size Biased Samples

	Provides functions and examples for testing hypothesis about the population mean and variance on samples drawn by r-size biased sampling schemes.
	"""
	
	cran = "RSizeBiased" 

	version("0.1.0", md5="be46629abfce7b655f83c067981d1c2f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMircomp(RPackage):
	"""Tools to assess and compare miRNA expression estimatation methods

	Based on a large miRNA dilution study, this package provides tools to read in the raw amplification data and use these data to assess the performance of methods that estimate expression from the amplification curves.
	"""
	
	bioc = "miRcomp"

	version("1.38.1", commit="146ec0ce2e56eb63fe3ca1f5adef587a29525fa1")
	version("1.32.0", commit="a13561f6395d31d22719d6681e8727843ef5cbf6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.22:", type=("build", "run"))
	depends_on("r-mircompdata", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))

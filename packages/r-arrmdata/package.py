# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrmdata(RPackage):
	"""Example dataset for normalization of Illumina 450k Methylation data

	Raw Beta values from 36 samples across 3 groups from Illumina 450k methylation arrays
	"""
	
	bioc = "ARRmData"

	version("1.44.0", commit="6c8d3a4af2421f3363aa624978181ba069375640")
	version("1.38.0", commit="81fb27786c6731fc078ddaa9a4cfab18308a4292")

	depends_on("r@3:", type=("build", "run"))


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMofadata(RPackage):
	"""Data package for Multi-Omics Factor Analysis (MOFA)

	A collection of datasets to accompany the R package MOFA and illustrate running and analysing MOFA models.
	"""
	
	bioc = "MOFAdata"

	version("1.24.0", commit="65717db0de077d3f4b0e995355ca15fa32b1ab6f")
	version("1.18.0", commit="f0c52b30320688b8e08abcd6cd532b914007cc4a")

	depends_on("r@3.5:", type=("build", "run"))


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyester(RPackage):
	"""Simulate RNA-seq reads

	This package can be used to simulate RNA-seq reads from differential expression experiments with replicates. The reads can then be aligned and used to perform comparisons of methods for differential expression.
	"""
	
	bioc = "polyester"

	version("1.38.0", commit="d7683461aec16e31bcba31bec70b7fffa926d667")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biostrings@2.32:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))

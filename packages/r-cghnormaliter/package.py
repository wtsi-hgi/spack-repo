# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghnormaliter(RPackage):
	"""Normalization of array CGH data with imbalanced aberrations.

	Normalization and centralization of array comparative genomic hybridization (aCGH) data. The algorithm uses an iterative procedure that effectively eliminates the influence of imbalanced copy numbers. This leads to a more reliable assessment of copy number alterations (CNAs).
	"""
	
	bioc = "CGHnormaliter"

	version("1.62.0", commit="c222298618c733aa86accdea28a3b19401798d5d")
	version("1.56.0", commit="6764dffe0d634baa79e2188d87fc21908446b62a")

	depends_on("r-cghcall", type=("build", "run"))
	depends_on("r-cghbase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

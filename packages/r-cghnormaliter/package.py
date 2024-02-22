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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CGHnormaliter_1.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CGHnormaliter/CGHnormaliter_1.56.0.tar.gz"]

	version("1.56.0", md5="948d3af66840226e7095e46d281df177")

	depends_on("r-cghcall", type=("build", "run"))
	depends_on("r-cghbase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

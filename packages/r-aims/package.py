# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAims(RPackage):
	"""Absolute Assignment of Breast Cancer Intrinsic Molecular Subtype.

	This package contains the AIMS implementation. It contains necessary
	functions to assign the five intrinsic molecular subtypes (Luminal A,
	Luminal B, Her2-enriched, Basal-like, Normal-like). Assignments could be
	done on individual samples as well as on dataset of gene expression
	data."""

	bioc = "AIMS"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AIMS_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AIMS/AIMS_1.34.0.tar.gz"]

	version("1.34.0", md5="23ef11145babcac9430b2c94db4dfae3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

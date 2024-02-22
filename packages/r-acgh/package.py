# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcgh(RPackage):
	"""Classes and functions for Array Comparative Genomic Hybridization data.

	Functions for reading aCGH data from image analysis output files and
	clone information files, creation of aCGH S3 objects for storing these
	data. Basic methods for accessing/replacing, subsetting, printing and
	plotting aCGH objects."""

	bioc = "aCGH"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/aCGH_1.80.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/aCGH/aCGH_1.80.0.tar.gz"]

	version("1.80.0", md5="137af76dc5756a83094da18eb0bededa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

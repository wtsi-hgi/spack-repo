# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarray(RPackage):
	"""Exploratory analysis for two-color spotted microarray data.

	Class definitions for two-color spotted microarray data. Fuctions for data
	input, diagnostic plots, normalization and quality checking."""

	bioc = "marray"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/marray_1.80.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/marray/marray_1.80.0.tar.gz"]

	version("1.80.0", md5="569b373e346d36964430d249d075cf07")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))

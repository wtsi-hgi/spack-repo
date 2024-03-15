# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenie3(RPackage):
	"""GEne Network Inference with Ensemble of trees.

	This package implements the GENIE3 algorithm for inferring gene
	regulatory networks from expression data."""

	bioc = "GENIE3"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GENIE3_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GENIE3/GENIE3_1.24.0.tar.gz"]

	version("1.24.0", md5="fb7d197e0e34175eba7dd31608aa67d6", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GENIE3_1.24.0.tar.gz")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

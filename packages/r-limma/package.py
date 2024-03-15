# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimma(RPackage):
	"""Linear Models for Microarray Data.

	Data analysis, linear models and differential expression for microarray
	data."""

	bioc = "limma"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/limma_3.58.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/limma/limma_3.58.1.tar.gz"]

	version("3.58.1", md5="f52a816d0d34b01f721654f90a1fb5f5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))

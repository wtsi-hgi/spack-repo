# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRots(RPackage):
	"""Reproducibility-Optimized Test Statistic.

	Calculates the Reproducibility-Optimized Test Statistic (ROTS) for
	differential testing in omics data."""

	bioc = "ROTS"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ROTS_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ROTS/ROTS_1.30.0.tar.gz"]

	version("1.30.0", md5="02d51e24e501790ad3049c1bb5b3f90b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

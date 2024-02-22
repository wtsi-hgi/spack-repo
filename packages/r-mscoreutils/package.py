# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscoreutils(RPackage):
	"""Core Utils for Mass Spectrometry Data.

	MsCoreUtils defines low-level functions for mass spectrometry data and is
	independent of any high-level data structures. These functions include mass
	spectra processing functions (noise estimation, smoothing, binning),
	quantitative aggregation functions (median polish, robust summarisation,
	...), missing data imputation, data normalisation (quantiles, vsn, ...) as
	well as misc helper functions, that are used across high-level data
	structure within the R for Mass Spectrometry packages."""

	bioc = "MsCoreUtils"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MsCoreUtils_1.14.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MsCoreUtils/MsCoreUtils_1.14.1.tar.gz"]

	version("1.14.1", md5="163cc129bc77ed033c124fed5bf7d9ca")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
	version("2.0.0", tag="RELEASE_3_21")
	version("1.8.0", commit="02e3c6455bb1afe7c4cc59ad6d4d8bae7b01428b")
	version("1.6.0", commit="3567ac1142ba97770b701ee8e5f9e3e6c781bd56")
	version("1.4.0", commit="2e656514a4bf5a837ee6e14ce9b28a61dab955e7")
	version("1.30.0", sha256="e66e3e66db24cbe8c324a68db09d6e00638d44337d88d5761c5a6e80ebe0a5fd")
	version("1.28.0", commit="032cb97ed6fe303758856c669a4f63fb9e43d124")
	version("1.26.0", commit="8bb45fe78779583ae4d30cf0dc3af0d8de405fdf")
	version("1.24.0", commit="372e4623b39f585d4196d21164436c1ba013173f")
	version("1.22.0", commit="a53ec77c40ed3b3c84e91d794c1602dd509cad83")
	version("1.18.0", commit="1d4e206a8ce68d5a1417ff51c26174ed9d0ba7d2")
	version("1.12.0", commit="7e2c96fd8fd36710321498745f24cc6b59ac02f0")
	version("1.10.1", commit="1733d3f868cef4d81af6edfc102221d80793937b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

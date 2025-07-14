# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConstand(RPackage):
	"""Data normalization by matrix raking

	Normalizes a data matrix `data` by raking (using the RAS method by Bacharach, see references) the Nrows by Ncols matrix such that the row means and column means equal 1. The result is a normalized data matrix `K=RAS`, a product of row mulipliers `R` and column multipliers `S` with the original matrix `A`. Missing information needs to be presented as `NA` values and not as zero values, because CONSTANd is able to ignore missing values when calculating the mean. Using CONSTANd normalization allows for the direct comparison of values between samples within the same and even across different CONSTANd-normalized data matrices.
	"""
	
	homepage = "qcquan.net/constand"
	bioc = "CONSTANd"

	version("1.16.0", commit="09b0c6a175e61be80e49c5f52d6ef71864fd5959")
	version("1.10.0", commit="151d7a9447fde6e4073343004bcd8d5aed04c73e")

	depends_on("r@4.1:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppparallel(RPackage):
	"""Parallel Programming Tools for 'Rcpp'.

	High level functions for parallel programming with 'Rcpp'. For example, the
	'parallelFor()' function can be used to convert the work of a standard
	serial "for" loop into a parallel one and the 'parallelReduce()' function
	can be used for accumulating aggregate or other values."""

	cran = "RcppParallel"

	version("5.1.7", md5="3eedbd5476fd033c472824996b339b73")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("intel-tbb", type=("build", "link", "run"))

	patch("asclang.patch", when="%fj")

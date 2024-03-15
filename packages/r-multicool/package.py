# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticool(RPackage):
	"""Permutations of multisets in cool-lex order.

	A set of tools to permute multisets without loops or hash tables and to
	generate integer partitions. The permutation functions are based on C code
	from Aaron Williams. Cool-lex order is similar to colexicographical order.
	The algorithm is described in Williams, A. (2009)
	<DOI:10.1145/1496770.1496877> Loopless Generation of Multiset Permutations
	by Prefix Shifts. Symposium on Discrete Algorithms, New York, United
	States. The permutation code is distributed without restrictions. The code
	for stable and efficient computation of multinomial coefficients comes from
	Dave Barber. The code can be download from
	<http://tamivox.org/dave/multinomial/code.html> and is distributed without
	conditions. The package also generates the integer partitions of a
	positive, non-zero integer n. The C++ code for this is based on Python code
	from Jerome Kelleher which can be found here
	<https://jeromekelleher.net/tag/integer-partitions.html>. The C++ code and
	Python code are distributed without conditions."""

	cran = "multicool"

	license("GPL-2.0-only")

	version("1.0.1", md5="864bdeb9e2eec4fbbe3fd77077b5e823")

	depends_on("r-rcpp", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInum(RPackage):
	"""Interval and Enum-Type Representation of Vectors.

	Enum-type representation of vectors and representation of intervals,
	including a method of coercing variables in data frames."""

	cran = "inum"

	version("1.0-5", md5="d639f582b8f3925f8c2ddc38febb2915")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-libcoin@1.0.0:", type=("build", "run"))

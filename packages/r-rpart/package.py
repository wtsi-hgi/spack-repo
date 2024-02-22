# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpart(RPackage):
	"""Recursive Partitioning and Regression Trees.

	Recursive partitioning for classification, regression and survival trees.
	An implementation of most of the functionality of the 1984 book by Breiman,
	Friedman, Olshen and Stone."""

	cran = "rpart"

	version("4.1.23", md5="3edb60e43c90b773588469edebc22596")

	depends_on("r@2.15:", type=("build", "run"))

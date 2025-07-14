# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrho(RPackage):
	"""Inference on agreement between ordered lists

	The package is aimed at inference on the amount of agreement in two sorted lists using the Rank-Rank Hypergeometric Overlap test.
	"""
	
	bioc = "RRHO"

	version("1.48.0", commit="5c177e46b8ce083618c841dfcb338f764bd8e6bc")
	version("1.42.0", commit="47c86bfeb2a58474bad7eb69f0bb3766f935efa5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchbox(RPackage):
	"""Utilities to train and validate classifiers based on pair switching using the K-Top-Scoring-Pair (KTSP) algorithm

	The package offer different classifiers based on comparisons of pair of features (TSP), using various decision rules (e.g., majority wins principle).
	"""
	
	bioc = "switchBox"

	version("1.44.0", commit="87668075d972759123db3fc2f5b9f9aaa5e79120")
	version("1.38.0", commit="f395d2ed8bdfaa603b5581b0b7569f1f973ff954")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))

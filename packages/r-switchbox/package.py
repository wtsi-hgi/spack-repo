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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/switchBox_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/switchBox/switchBox_1.38.0.tar.gz"]

	version("1.38.0", md5="29de2be8446a4f686acf75635f1539b9")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))

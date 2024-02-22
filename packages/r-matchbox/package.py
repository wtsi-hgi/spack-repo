# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchbox(RPackage):
	"""Utilities to compute, compare, and plot the agreement between ordered vectors of features (ie. distinct genomic experiments). The package includes Correspondence-At-the-TOP (CAT) analysis.

	The matchBox package enables comparing ranked vectors of features, merging multiple datasets, removing redundant features, using CAT-plots and Venn diagrams, and computing statistical significance.
	"""
	
	bioc = "matchBox" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/matchBox_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/matchBox/matchBox_1.44.0.tar.gz"]

	version("1.44.0", md5="b6e4b10ee38f433d1bce146a089a44ec")

	depends_on("r@2.8:", type=("build", "run"))

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

	version("1.50.0", commit="82464cea3f56b6d25632f0184af721b94cb5bcc6")
	version("1.44.0", commit="d862734765357d7982ad16ec7170beb60c0119e9")

	depends_on("r@2.8:", type=("build", "run"))

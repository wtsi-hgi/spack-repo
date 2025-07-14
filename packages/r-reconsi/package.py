# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReconsi(RPackage):
	"""Resampling Collapsed Null Distributions for Simultaneous Inference

	Improves simultaneous inference under dependence of tests by estimating a collapsed null distribution through resampling. Accounting for the dependence between tests increases the power while reducing the variability of the false discovery proportion. This dependence is common in genomics applications, e.g. when combining flow cytometry measurements with microbiome sequence counts.
	"""
	
	bioc = "reconsi"

	version("1.20.0", commit="d0ba92fb12885dd88605cacd430fb082b705e0ed")
	version("1.14.0", commit="92e22ca4d7cf9c3c37de4ad05aa8cc7246cffa61")

	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

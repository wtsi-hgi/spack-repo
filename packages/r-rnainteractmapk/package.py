# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnainteractmapk(RPackage):
	"""Mapping of Signalling Networks through Synthetic Genetic Interaction Analysis by RNAi

	This package includes all data used in the paper -Mapping of Signalling Networks through Synthetic Genetic Interaction Analysis by RNAi- by Horn, Sandmann, Fischer et al.., Nat. Methods, 2011. The package vignette shows the R code to reproduce all figures in the paper.
	"""
	
	bioc = "RNAinteractMAPK"

	version("1.40.0", commit="e0cd34cb032d667147a8ae968e2ead65b4626210")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-sparselda", type=("build", "run"))
	depends_on("r-rnainteract", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))


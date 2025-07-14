# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhilr(RPackage):
	"""Phylogenetic partitioning based ILR transform for metagenomics data

	PhILR is short for Phylogenetic Isometric Log-Ratio Transform. This package provides functions for the analysis of compositional data (e.g., data representing proportions of different variables/parts). Specifically this package allows analysis of compositional data where the parts can be related through a phylogenetic tree (as is common in microbiota survey data) and makes available the Isometric Log Ratio transform built from the phylogenetic tree and utilizing a weighted reference measure.
	"""
	
	homepage = "https://github.com/jsilve24/philr"
	bioc = "philr"

	version("1.34.0", commit="1d9ba3bbf04f84be160b250e3165a7b563772de4")
	version("1.28.0", commit="97ee2ead8184b88e4b5b47428dc2798e5464620c")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))

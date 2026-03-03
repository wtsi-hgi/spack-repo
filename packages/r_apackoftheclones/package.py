# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApackoftheclones(RPackage):
	"""Visualization of Clonal Expansion for Single Cell Immune
Profiles

	Visualize clonal expansion via circle-packing. 'APackOfTheClones' extends 'scRepertoire' to produce a publication-ready visualization of clonal expansion at a single cell resolution, by representing expanded clones as differently sized circles. The method was originally implemented by Murray Christian and Ben Murrell in the following immunology study: Ma et al. (2021) <doi:10.1126/sciimmunol.abg6356>.
	"""
	
	homepage = "https://qile0317.github.io/APackOfTheClones/"
	cran = "APackOfTheClones" 

	version("1.0.0", md5="24d7aa6a72a8ed952f4bda383ec3c656")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))

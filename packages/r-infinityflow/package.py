# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfinityflow(RPackage):
	"""Augmenting Massively Parallel Cytometry Experiments Using Multivariate Non-Linear Regressions

	Pipeline to analyze and merge data files produced by BioLegend's LEGENDScreen or BD Human Cell Surface Marker Screening Panel (BD Lyoplates).
	"""
	
	bioc = "infinityFlow"

	version("1.18.0", commit="7c232d8d4292c5373f9d38c92c16329660355044")
	version("1.12.0", commit="5649007d280db4cc5a7c7ce629be5229dbd3cb05")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))

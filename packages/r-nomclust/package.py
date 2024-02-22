# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNomclust(RPackage):
	"""Hierarchical Cluster Analysis of Nominal Data

	Similarity measures for hierarchical clustering of objects characterized by
    nominal (categorical) variables. Evaluation criteria for nominal data clustering.
	"""
	
	cran = "nomclust" 

	version("2.8.0", md5="1d0aa4aa7414cfa408f90d21cd753f83")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdaccaHp(RPackage):
	"""Hierarchical and Variation Partitioning for Canonical Analysis

	This function conducts variation partitioning and hierarchical partitioning to calculate the unique, shared (referred as to "common") and individual contributions of each predictor (or matrix) towards explained variation (R-square and adjusted R-square) on canonical analysis (RDA,CCA and db-RDA), applying the algorithm of Lai J.,Zou Y., Zhang J.,Peres-Neto P.(2022) Generalizing hierarchical and variation partitioning in multiple regression and canonical analyses using the rdacca.hp R package.Methods in Ecology and Evolution,13: 782-788 <DOI:10.1111/2041-210X.13800>. 
	"""
	
	homepage = "https://github.com/laijiangshan/rdacca.hp"
	cran = "rdacca.hp" 

	version("1.1-0", md5="917f125922b7885c0f49b00200f07216")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

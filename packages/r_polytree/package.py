# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolytree(RPackage):
	"""Estimate Causal Polytree from Data

	Given a data matrix with rows representing data vectors and columns representing variables, produces a directed polytree for the underlying causal structure. Based on the algorithm developed in Chatterjee and Vidyasagar (2022) <arxiv:2209.07028>. The method is fully nonparametric, making no use of linearity assumptions, and especially useful when the number of variables is large.
	"""
	
	cran = "PolyTree" 

	version("0.0.1", md5="89c6872c734318f93ebbb1528dff61d6")

	depends_on("r-foci", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))

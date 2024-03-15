# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGromovlab(RPackage):
	"""Gromov-Hausdorff Type Distances for Labeled Metric Spaces

	Computes Gromov-Hausdorff type l^p distances for labeled metric spaces. These distances were introduced in V.Liebscher, Gromov meets Phylogenetics - new Animals for the Zoo of Metrics on Tree Space <arXiv:1504.05795>  for phylogenetic trees, but may apply to a diversity of scenarios. 
	"""
	
	cran = "gromovlab" 

	version("0.8-3", md5="2ba673a0236ff67970886bc482c6e889")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-glpkapi", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))

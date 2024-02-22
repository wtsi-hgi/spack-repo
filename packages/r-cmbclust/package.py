# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmbclust(RPackage):
	"""Conditional Mixture Modeling and Model-Based Clustering

	Conditional mixture model fitted via EM (Expectation Maximization) algorithm for model-based clustering, including parsimonious procedure, optimal conditional order exploration, and visualization.
	"""
	
	cran = "cmbClust" 

	version("0.0.1", md5="a00a6fc7fbda778436513b51125494c8")

	depends_on("r@3.5:", type=("build", "run"))

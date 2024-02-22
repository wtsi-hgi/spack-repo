# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylin(RPackage):
	"""Spatial Interpolation of Genetic Data

	The spatial interpolation of genetic distances between
	     samples is based on a modified kriging method that
	     accepts a genetic distance matrix and generates a map of
	     probability of lineage presence. This package also offers
	     tools to generate a map of  potential contact zones
	     between groups with user-defined thresholds in the tree
	     to account for old and recent divergence. Additionally,
	     it has functions for IDW interpolation using genetic data
	     and midpoints.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "phylin" 

	version("2.0.2", md5="d7ac4716c80f5342eda986edfde28b69")


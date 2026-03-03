# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsegrid(RPackage):
	"""Sparse grid integration in R

	SparseGrid is a package to create sparse grids for numerical integration, based on code from www.sparse-grids.de
	"""
	
	cran = "SparseGrid" 

	version("0.8.2", md5="e54f03330531251834c39d33d877b9bf")


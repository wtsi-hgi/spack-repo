# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChameleon(RPackage):
	"""Automatic Colors for Multi-Dimensional Data

	Assign distinct colors to arbitrary multi-dimensional data, considering its structure.
	"""
	
	cran = "chameleon" 

	version("0.2-3", md5="2508859ce9c2154be4ff8b2b94951e0e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))

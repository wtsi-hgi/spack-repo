# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaco(RPackage):
	"""Procrustes Application to Cophylogenetic Analysis

	Procrustes analyses to infer co-phylogenetic
    matching between pairs of phylogenetic trees.
	"""
	
	homepage = "https://www.uv.es/cophylpaco/"
	cran = "paco" 

	version("0.4.2", md5="c9f44419d5e4e5997fc76e4107ce0c71")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-vegan@2.2.0:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))

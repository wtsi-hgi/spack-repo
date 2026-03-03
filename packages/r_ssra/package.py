# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsra(RPackage):
	"""Sakai Sequential Relation Analysis

	Takeya Semantic Structure Analysis (TSSA) and Sakai Sequential Relation Analysis (SSRA)
             for polytomous items for examining whether each pair of items has a sequential or equal
             relation. Package includes functions for generating a sequential relation table and a
             treegram to visualize sequential or equal relations between pairs of items.
	"""
	
	cran = "SSRA" 

	version("0.1-0", md5="3cfe42b91abd941205179f963eca8d8e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

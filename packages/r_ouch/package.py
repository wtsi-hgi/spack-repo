# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROuch(RPackage):
	"""Ornstein-Uhlenbeck Models for Phylogenetic Comparative
Hypotheses

	Fit and compare Ornstein-Uhlenbeck models for evolution along a phylogenetic tree.
	"""
	
	homepage = "https://kingaa.github.io/ouch/"
	cran = "ouch" 

	version("2.19", md5="c2c56a0294c6a50a182b925db43bff8c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))

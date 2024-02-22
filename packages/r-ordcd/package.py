# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdcd(RPackage):
	"""Ordinal Causal Discovery

	Algorithms for ordinal causal discovery. This package aims to enable users to discover causality for observational ordinal categorical data with greedy and exhaustive search. See Ni, Y., & Mallick, B. (2022) <https://proceedings.mlr.press/v180/ni22a/ni22a.pdf> "Ordinal Causal Discovery. Proceedings of the 38th Conference on Uncertainty in Artificial Intelligence, (UAI 2022), PMLR 180:1530–1540".
	"""
	
	homepage = "https://github.com/nySTAT/OrdCD"
	cran = "OrdCD" 

	version("1.1.2", md5="a7c238a517d46c71cc14c588db842e50")

	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

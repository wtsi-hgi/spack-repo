# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProps(RPackage):
	"""PRObabilistic Pathway Score (PROPS)

	This package calculates probabilistic pathway scores using gene expression data. Gene expression values are aggregated into pathway-based scores using Bayesian network representations of biological pathways.
	"""
	
	bioc = "PROPS"

	version("1.30.0", commit="8111b33c6507619c75ff2f143d7068ed4db8c490")
	version("1.24.0", commit="542f64cd079294e67c71a98e49024d5419faac08")

	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

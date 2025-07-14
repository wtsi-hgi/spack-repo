# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowmerge(RPackage):
	"""Cluster Merging for Flow Cytometry Data

	Merging of mixture components for model-based automated gating of flow cytometry data using the flowClust framework. Note: users should have a working copy of flowClust 2.0 installed.
	"""
	
	bioc = "flowMerge"

	version("2.56.0", commit="6dabf909ea01aedea2cf60def0680f1a7973be7b")
	version("2.50.0", commit="dec533083d0af8850c527b8533da8dacd37b4071")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-feature", type=("build", "run"))
	depends_on("r-flowclust", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))

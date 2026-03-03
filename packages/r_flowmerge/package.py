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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowMerge_2.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowMerge/flowMerge_2.50.0.tar.gz"]

	version("2.50.0", md5="c0d4d124e3d94a0eab8fc138f9044d2c")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-feature", type=("build", "run"))
	depends_on("r-flowclust", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowworkspace(RPackage):
	"""Infrastructure for representing and interacting with gated and ungated cytometry data sets.

	This package is designed to facilitate comparison of automated gating methods against manual gating done in flowJo. This package allows you to import basic flowJo workspaces into BioConductor and replicate the gating from flowJo using the flowCore functionality. Gating hierarchies, groups of samples, compensation, and transformation are performed so that the output matches the flowJo analysis.
	"""
	
	bioc = "flowWorkspace" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowWorkspace_4.14.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowWorkspace/flowWorkspace_4.14.3.tar.gz"]

	version("4.20.0", tag="RELEASE_3_21")
	version("4.14.3", sha256="9c8fdf2ced1db2e64f1673d6796618a3b1c813b9b92d358b2c82181dfffe161e")
	version("4.14.2", md5="8c13b6aa80732d54f36bb544adba5a6c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-cytolib@2.3.7:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rprotobuflib@1.99.4:", type=("build", "run"))
	depends_on("r-flowcore@2.1.1:", type=("build", "run"))
	depends_on("r-ncdfflow@2.25.4:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-bh@1.62.0.1:", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

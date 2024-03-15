# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAttract(RPackage):
	"""Methods to Find the Gene Expression Modules that Represent the Drivers of Kauffman's Attractor Landscape

	This package contains the functions to find the gene expression modules that represent the drivers of Kauffman's attractor landscape. The modules are the core attractor pathways that discriminate between different cell types of groups of interest. Each pathway has a set of synexpression groups, which show transcriptionally-coordinated changes in gene expression.
	"""
	
	bioc = "attract" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/attract_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/attract/attract_1.54.0.tar.gz"]

	version("1.54.0", md5="e7d563026d5d00b5dd3bd906268af221")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-reactome-db", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))

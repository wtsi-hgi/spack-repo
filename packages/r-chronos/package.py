# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChronos(RPackage):
	"""CHRONOS: A time-varying method for microRNA-mediated sub-pathway enrichment analysis

	A package used for efficient unraveling of the inherent dynamic properties of pathways. MicroRNA-mediated subpathway topologies are extracted and evaluated by exploiting the temporal transition and the fold change activity of the linked genes/microRNAs.
	"""
	
	bioc = "CHRONOS"

	version("1.36.0", commit="6e103dd9360aa815326d1c004291eb257266c263")
	version("1.30.0", commit="553c13131e040763c5f104070764cecdb4db628e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
	depends_on("pandoc", type=("build", "link", "run"))

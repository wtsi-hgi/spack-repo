# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRontotools(RPackage):
	"""R Onto-Tools suite

	Suite of tools for functional analysis.
	"""
	
	bioc = "ROntoTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ROntoTools_2.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ROntoTools/ROntoTools_2.30.0.tar.gz"]

	version("2.36.0", tag="RELEASE_3_21")
	version("2.30.0", sha256="b1033239dc62910eb2227b8bd37c86c5fb19a2214c20b8e37079ca970485fbdc")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))

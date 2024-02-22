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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ROntoTools_2.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ROntoTools/ROntoTools_2.30.0.tar.gz"]

	version("2.30.0", md5="11764a125b9411a5b2d2ba20f4c64024")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbkegg(RPackage):
	"""biodbKegg, a library for connecting to the KEGG Database

	The biodbKegg library is an extension of the biodb framework package that provides access to the KEGG databases Compound, Enzyme, Genes, Module, Orthology and Reaction. It allows to retrieve entries by their accession numbers. Web services like "find", "list" and "findExactMass" are also available. Some functions for navigating along the pathways have also been implemented.
	"""
	
	homepage = "https://github.com/pkrog/biodbKegg"
	bioc = "biodbKegg" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/biodbKegg_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/biodbKegg/biodbKegg_1.8.0.tar.gz"]

	version("1.8.0", md5="868600b40fc5ce4c38ced82df890400d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-biodb@1.4.2:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))

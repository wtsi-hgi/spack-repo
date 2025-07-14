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

	version("1.8.0", commit="6c54c2ddece3aa39116690829979b4bcff458787")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-biodb@1.4.2:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))

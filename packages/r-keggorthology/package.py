# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggorthology(RPackage):
	"""graph support for KO, KEGG Orthology

	graphical representation of the Feb 2010 KEGG Orthology. The KEGG orthology is a set of pathway IDs that are not to be confused with the KEGG ortholog IDs.
	"""
	
	bioc = "keggorthology" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/keggorthology_2.54.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/keggorthology/keggorthology_2.54.0.tar.gz"]

	version("2.54.0", md5="56d510a339dd4fb984bad81624d83142")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-hgu95av2-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))

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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/keggorthology_2.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/keggorthology/keggorthology_2.54.0.tar.gz"]

	version("2.60.0", tag="RELEASE_3_21")
	version("2.54.0", sha256="49d419f2a8d206ef7443aeaf1508735e6df18a5d1c376985966e7d8828c16659")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-hgu95av2-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))

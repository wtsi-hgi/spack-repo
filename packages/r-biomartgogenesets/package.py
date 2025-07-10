# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomartgogenesets(RPackage):
	"""Gene Ontology Gene Sets from BioMart

	It contains pre-compiled Gene Ontology gene sets for all organisms available on the Ensembl database. It also includes GO gene sets for organisms on Ensembl Plants, Ensembl Metazoa, Ensembl Fungi and Ensembl Protists. The data was collected with the biomaRt package.
	"""
	
	homepage = "https://github.com/jokergoo/BioMartGOGeneSets"
	bioc = "BioMartGOGeneSets" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BioMartGOGeneSets_0.99.11.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BioMartGOGeneSets/BioMartGOGeneSets_0.99.11.tar.gz"]

	version("0.99.11", sha256="385ebed5be80df4310ca401ab5c9d637ffcc2f71c99a80f42be17d80c34693a9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))


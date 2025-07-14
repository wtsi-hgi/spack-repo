# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhpathbankdbs(RPackage):
	"""Metabolites and proteins linked to PathBank pathways (for AnnotationHub)

	The package provides a comprehensive mapping table of metabolites and proteins linked to PathBank pathways. The tables include HMDB, KEGG, ChEBI, CAS, Drugbank, Uniprot IDs. The tables are provided for each of the 10 species ("Homo sapiens", "Escherichia coli", "Mus musculus", "Arabidopsis thaliana", "Saccharomyces cerevisiae", "Bos taurus", "Caenorhabditis elegans", "Rattus norvegicus", "Drosophila melanogaster", and "Pseudomonas aeruginosa"). These table information can be used for Metabolite Set (and other) Enrichment Analysis.
	"""
	
	homepage = "https://github.com/kozo2/AHPathbankDbs"
	bioc = "AHPathbankDbs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AHPathbankDbs_0.99.5.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/AHPathbankDbs/AHPathbankDbs_0.99.5.tar.gz"]

    version("0.99.5", tag="RELEASE_3_21")
	version("0.99.5", sha256="09dd1c5be5712a64a07d1b1cfcc19f37bc2dd76c69b0bf5c663d8852e9cb8c83")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.23:", type=("build", "run"))


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhwikipathwaysdbs(RPackage):
	"""Metabolites linked to WikiPathways pathways (for AnnotationHub)

	The package provides a comprehensive mapping table of metabolites linked to Wikipathways pathways. The tables include HMDB, KEGG, ChEBI, Drugbank, PubChem compound, ChemSpider, KNApSAcK, and Wikidata IDs plus CAS and InChIKey. The tables are provided for each of the 25 species ("Anopheles gambiae", "Arabidopsis thaliana", "Bacillus subtilis", "Bos taurus", "Caenorhabditis elegans", "Canis familiaris", "Danio rerio", "Drosophila melanogaster", "Equus caballus", "Escherichia coli", "Gallus gallus", "Gibberella zeae", "Homo sapiens", "Hordeum vulgare", "Mus musculus", "Mycobacterium tuberculosis", "Oryza sativa", "Pan troglodytes", "Plasmodium falciparum", "Populus trichocarpa", "Rattus norvegicus", "Saccharomyces cerevisiae", "Solanum lycopersicum", "Sus scrofa", "Zea mays"). These table information can be used for Metabolite Set Enrichment Analysis.
	"""
	
	homepage = "https://github.com/kozo2/AHWikipathwaysDbs"
	bioc = "AHWikipathwaysDbs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AHWikipathwaysDbs_0.99.4.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/AHWikipathwaysDbs/AHWikipathwaysDbs_0.99.4.tar.gz"]

	version("0.99.4", sha256="04036684f888d233250b583ee8c5be23e045e781ce019c13fd7c99d175bae36f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.23:", type=("build", "run"))


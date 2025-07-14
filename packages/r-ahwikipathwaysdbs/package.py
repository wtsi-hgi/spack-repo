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

	version("0.99.4", commit="04edc62328d2a94c8b345bac188df41a8f04c199")
	version("0.99.4", commit="04edc62328d2a94c8b345bac188df41a8f04c199")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.23:", type=("build", "run"))


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarfrompdb(RPackage):
	"""Disease-Gene-Variant Relations Mining from the Public Databases
and Literature

	Captures and compiles the genes and variants related to a disease, a phenotype or a clinical feature from the public databases including HPO (Human Phenotype Ontology, <http://human-phenotype-ontology.github.io/about.html>), Orphanet <http://www.orpha.net/consor/cgi-bin/index.php>, OMIM (Online Mendelian Inheritance in Man, <http://www.omim.org>), ClinVar <http://www.ncbi.nlm.nih.gov/clinvar>, and UniProt (Universal Protein Resource, <http://www.uniprot.org>) and PubMed abstracts. HPO provides a standardized vocabulary of phenotypic abnormalities encountered in human disease. HPO currently contains approximately 11,000 terms and over 115,000 annotations to hereditary diseases. Orphanet is the reference portal for information on rare diseases and orphan drugs, whose aim is to help improve the diagnosis, care and treatment of patients with rare diseases. OMIM is a continuously updated catalog of human genes and genetic disorders and traits, with particular focus on the molecular relationship between genetic variation and phenotypic expression. ClinVar is a freely accessible, public archive of reports of the relationships among human variations and phenotypes, with supporting evidence. UniProt focuses on amino acid altering variants imported from Ensembl Variation databases. For Homo sapiens, the variants including human polymorphisms and disease mutations in the UniProt are manually curated  from UniProtKB/Swiss-Prot. Additionally, PubMed provides the primary and latest source of the information. Text mining was employed to capture the information from PubMed abstracts. 
	"""
	
	cran = "VarfromPDB" 

	version("2.2.10", md5="b7c92586fba4a698d4b488ba35eb2fbe")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2r", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rismed", type=("build", "run"))

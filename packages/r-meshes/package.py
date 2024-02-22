# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeshes(RPackage):
	"""MeSH Enrichment and Semantic analyses

	MeSH (Medical Subject Headings) is the NLM controlled vocabulary used to manually index articles for MEDLINE/PubMed. MeSH terms were associated by Entrez Gene ID by three methods, gendoo, gene2pubmed and RBBH. This association is fundamental for enrichment and semantic analyses. meshes supports enrichment analysis (over-representation and gene set enrichment analysis) of gene list or whole expression profile. The semantic comparisons of MeSH terms provide quantitative ways to compute similarities between genes and gene groups. meshes implemented five methods proposed by Resnik, Schlicker, Jiang, Lin and Wang respectively and supports more than 70 species.
	"""
	
	homepage = "https://yulab-smu.top/biomedical-knowledge-mining-book/"
	bioc = "meshes" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/meshes_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/meshes/meshes_1.28.0.tar.gz"]

	version("1.28.0", md5="90be6eeeb3ced1146ddcba48e2ec6c6e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-meshdbi", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))

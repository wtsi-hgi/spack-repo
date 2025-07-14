# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcistarget(RPackage):
	"""RcisTarget Identify transcription factor binding motifs enriched on a list of genes or genomic regions

	RcisTarget identifies transcription factor binding motifs (TFBS) over-represented on a gene list. In a first step, RcisTarget selects DNA motifs that are significantly over-represented in the surroundings of the transcription start site (TSS) of the genes in the gene-set. This is achieved by using a database that contains genome-wide cross-species rankings for each motif. The motifs that are then annotated to TFs and those that have a high Normalized Enrichment Score (NES) are retained. Finally, for each motif and gene-set, RcisTarget predicts the candidate target genes (i.e. genes in the gene-set that are ranked above the leading edge).
	"""
	
	homepage = "http://scenic.aertslab.org"
	bioc = "RcisTarget" 

	version("1.28.1", commit="d3afd220f4374e422a07a61f2df4b65b331b1d05")
	version("1.22.0", commit="49974d11c68185406c0f66637d9a9981408f0919")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aucell@1.1.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-arrow@2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

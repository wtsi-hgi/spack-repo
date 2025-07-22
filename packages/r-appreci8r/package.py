# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppreci8r(RPackage):
	"""appreci8R: an R/Bioconductor package for filtering SNVs and short indels with high sensitivity and high PPV

	The appreci8R is an R version of our appreci8-algorithm - A Pipeline for PREcise variant Calling Integrating 8 tools. Variant calling results of our standard appreci8-tools (GATK, Platypus, VarScan, FreeBayes, LoFreq, SNVer, samtools and VarDict), as well as up to 5 additional tools is combined, evaluated and filtered.
	"""
	
	bioc = "appreci8R"

	version("1.26.0", commit="f62d6977f675e23b53d3d9b65699b600eb7a7972")
	version("1.20.2", commit="491a34d7a8c664d6564c3179151ee90854d81546")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-snplocs-hsapiens-dbsnp144-grch37", type=("build", "run"))
	depends_on("r-xtrasnplocs-hsapiens-dbsnp144-grch37", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-mafdb-1kgenomes-phase3-hs37d5", type=("build", "run"))
	depends_on("r-mafdb-exac-r1-0-hs37d5", type=("build", "run"))
	depends_on("r-mafdb-gnomadex-r2-1-hs37d5", type=("build", "run"))
	depends_on("r-cosmic-67", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-polyphen-hsapiens-dbsnp131", type=("build", "run"))
	depends_on("r-sift-hsapiens-dbsnp137", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

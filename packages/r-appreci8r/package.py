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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/appreci8R_1.20.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/appreci8R/appreci8R_1.20.2.tar.gz"]

	version("1.20.2", sha256="52003d9e9f3180678d3b09ee28358d42a4834d9128024d63f20b49a2cd332a63")

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

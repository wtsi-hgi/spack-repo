# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg38Dbsnp151Major(RPackage):
	"""Full genome sequences for Homo sapiens (UCSC version hg38, based on GRCh38.p12) with injected major alleles (dbSNP151)

	Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg38, based on GRCh38.p12) with major allele injected from dbSNP151, and stored in Biostrings objects. Only single nucleotide variants (SNVs) were considered. At each SNV, the most frequent allele was chosen at the major allele to be injected into the reference genome.
	"""
	
	bioc = "BSgenome.Hsapiens.UCSC.hg38.dbSNP151.major" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg38.dbSNP151.major_0.0.9999.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg38.dbSNP151.major/BSgenome.Hsapiens.UCSC.hg38.dbSNP151.major_0.0.9999.tar.gz"]

	version("0.0.9999", md5="c59f66e52d4982942bea2254223d58df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome@1.56:", type=("build", "run"))

	# annotation
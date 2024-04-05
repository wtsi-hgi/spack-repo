# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtrasnplocsHsapiensDbsnp144Grch37(RPackage):
	"""Extra SNP locations for Homo sapiens (dbSNP Build 144)

	Extra SNP locations and alleles for Homo sapiens extracted from NCBI dbSNP Build 144. The source data files used for this package were created by NCBI on May 29-30, 2015, and contain SNPs mapped to reference genome GRCh37.p13 (a patched version of GRCh37 that doesn't alter chromosomes 1-22, X, Y, MT). While the SNPlocs.Hsapiens.dbSNP144.GRCh37 package contains only molecular variations of class "snp", this package contains molecular variations of other classes (in-del, heterozygous, microsatellite, named-locus, no-variation, mixed, and multinucleotide-polymorphism).
	"""
	
	bioc = "XtraSNPlocs.Hsapiens.dbSNP144.GRCh37" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/XtraSNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.12.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/XtraSNPlocs.Hsapiens.dbSNP144.GRCh37/XtraSNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.12.tar.gz"]

	version("0.99.12", md5="758d024c50d2349036dc27cc689b4e5a", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/XtraSNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.12.tar.gz")
	version("0.99.12", md5="758d024c50d2349036dc27cc689b4e5a", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/XtraSNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.12.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))


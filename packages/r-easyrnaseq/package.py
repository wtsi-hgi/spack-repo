# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyrnaseq(RPackage):
	"""Count summarization and normalization for RNA-Seq data

	Calculates the coverage of high-throughput short-reads against a genome of reference and summarizes it per feature of interest (e.g. exon, gene, transcript). The data can be normalized as 'RPKM' or by the 'DESeq' or 'edgeR' package.
	"""
	
	bioc = "easyRNASeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/easyRNASeq_2.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/easyRNASeq/easyRNASeq_2.38.0.tar.gz"]

    version("2.44.0", tag="RELEASE_3_21")
	version("2.38.0", sha256="ff0a8a4472bfd493ea80d8013d367e35c9d8a2042637658adb2fe089925c3942")

	depends_on("r-biobase@2.50:", type=("build", "run"))
	depends_on("r-biocfilecache@1.14:", type=("build", "run"))
	depends_on("r-biocgenerics@0.36:", type=("build", "run"))
	depends_on("r-biocparallel@1.24.1:", type=("build", "run"))
	depends_on("r-biomart@2.46:", type=("build", "run"))
	depends_on("r-biostrings@2.58:", type=("build", "run"))
	depends_on("r-edger@3.32:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.26:", type=("build", "run"))
	depends_on("r-genomeintervals@1.46:", type=("build", "run"))
	depends_on("r-genomicalignments@1.26:", type=("build", "run"))
	depends_on("r-genomicranges@1.42:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.20:", type=("build", "run"))
	depends_on("r-iranges@2.24:", type=("build", "run"))
	depends_on("r-lsd@4.1.0:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
	depends_on("r-rsamtools@2.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.28:", type=("build", "run"))
	depends_on("r-shortread@1.48:", type=("build", "run"))

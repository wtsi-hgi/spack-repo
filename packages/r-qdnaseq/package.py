# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdnaseq(RPackage):
	"""Quantitative DNA Sequencing for Chromosomal Aberrations

	Quantitative DNA sequencing for chromosomal aberrations. The genome is divided into non-overlapping fixed-sized bins, number of sequence reads in each counted, adjusted with a simultaneous two-dimensional loess correction for sequence mappability and GC content, and filtered to remove spurious regions in the genome. Downstream steps of segmentation and calling are also implemented via packages DNAcopy and CGHcall, respectively.
	"""
	
	homepage = "https://github.com/ccagc/QDNAseq"
	bioc = "QDNAseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/QDNAseq_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/QDNAseq/QDNAseq_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="7a5681d90baeeb8dc5878163b5692b8851cdd1bb564fa67dd80e0e8ef1b358d8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biobase@2.18:", type=("build", "run"))
	depends_on("r-cghbase@1.18:", type=("build", "run"))
	depends_on("r-cghcall@2.18:", type=("build", "run"))
	depends_on("r-dnacopy@1.32:", type=("build", "run"))
	depends_on("r-genomicranges@1.20:", type=("build", "run"))
	depends_on("r-iranges@2.2:", type=("build", "run"))
	depends_on("r-matrixstats@0.60:", type=("build", "run"))
	depends_on("r-r-utils@2.9:", type=("build", "run"))
	depends_on("r-rsamtools@1.20:", type=("build", "run"))
	depends_on("r-future-apply@1.8.1:", type=("build", "run"))

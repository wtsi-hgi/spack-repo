# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylkit(RPackage):
	"""DNA methylation analysis from high-throughput bisulfite sequencing results

	methylKit is an R package for DNA methylation analysis and annotation from high-throughput bisulfite sequencing. The package is designed to deal with sequencing data from RRBS and its variants, but also target-capture methods and whole genome bisulfite sequencing. It also has functions to analyze base-pair resolution 5hmC data from experimental protocols such as oxBS-Seq and TAB-Seq. Methylation calling can be performed directly from Bismark aligned BAM files.
	"""
	
	homepage = "https://github.com/al2na/methylKit"
	bioc = "methylKit" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methylKit_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methylKit/methylKit_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="3b363dd0daca050d736ce36b683d959a0ce6fc5e7e536fc71395ae5988e28578")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges@1.18.1:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.13.13:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-fastseg", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))

# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeseq2(RPackage):
	"""Differential gene expression analysis based on the negative binomial
	distribution.

	Estimate variance-mean dependence in count data from high-throughput
	sequencing assays and test for differential expression based on a model
	using the negative binomial distribution."""

	homepage = "https://bioconductor.org/packages/DESeq2"
	git = "https://git.bioconductor.org/packages/DESeq2.git"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DESeq2_1.42.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DESeq2/DESeq2_1.42.1.tar.gz"]

	version("1.42.1", md5="7b8f94401f376261f869ee839a0be2e1", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DESeq2_1.42.1.tar.gz")

	depends_on("r-s4vectors@0.23.18:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.1.6:", type=("build", "run"))
	depends_on("r-biocgenerics@0.7.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

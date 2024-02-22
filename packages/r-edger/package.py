# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdger(RPackage):
	"""Empirical Analysis of Digital Gene Expression Data in R.

	Differential expression analysis of RNA-seq expression profiles with
	biological replication. Implements a range of statistical methodology
	based on the negative binomial distributions, including empirical Bayes
	estimation, exact tests, generalized linear models and quasi-likelihood
	tests. As well as RNA-seq, it be applied to differential signal analysis
	of other types of genomic data that produce counts, including ChIP-seq,
	Bisulfite-seq, SAGE and CAGE."""

	bioc = "edgeR"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/edgeR_4.0.16.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/edgeR/edgeR_4.0.16.tar.gz"]

	version("4.0.16", md5="8fb1c6c67e29d299c991d16d0f6c5f5b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-limma@3.41.5:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

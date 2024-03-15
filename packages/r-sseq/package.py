# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSseq(RPackage):
	"""Shrinkage estimation of dispersion in Negative Binomial models for RNA-
	seq experiments with small sample size.

	The purpose of this package is to discover the genes that are
	differentially expressed between two conditions in RNA-seq experiments.
	Gene expression is measured in counts of transcripts and modeled with
	the Negative Binomial (NB) distribution using a shrinkage approach for
	dispersion estimation. The method of moment (MM) estimates for
	dispersion are shrunk towards an estimated target, which minimizes the
	average squared difference between the shrinkage estimates and the
	initial estimates. The exact per-gene probability under the NB model is
	calculated, and used to test the hypothesis that the expected expression
	of a gene in two conditions identically follow a NB distribution."""

	bioc = "sSeq"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sSeq_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sSeq/sSeq_1.40.0.tar.gz"]

	version("1.40.0", md5="9276919acd944871a6e05a8dbeed6b9f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))

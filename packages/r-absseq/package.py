# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbsseq(RPackage):
	"""ABSSeq: a new RNA-Seq analysis method based on modelling absolute
	expression differences.

	Inferring differential expression genes by absolute counts difference
	between two groups, utilizing Negative binomial distribution and
	moderating fold-change according to heterogeneity of dispersion across
	expression level."""

	bioc = "ABSSeq"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ABSSeq_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ABSSeq/ABSSeq_1.56.0.tar.gz"]

	version("1.56.0", md5="d170bf2f9a37dcdffd2d91e233ce5132")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))

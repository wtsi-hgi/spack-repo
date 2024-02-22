# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAldex2(RPackage):
	"""Analysis Of Differential Abundance Taking Sample Variation Into Account.

	A differential abundance analysis for the comparison of two or more
	conditions. Useful for analyzing data from standard RNA-seq or meta-RNA-
	seq assays as well as selected and unselected values from in-vitro
	sequence selections. Uses a Dirichlet-multinomial model to infer
	abundance from counts, optimized for three or more experimental
	replicates. The method infers biological and sampling variation to
	calculate the expected false discovery rate, given the variation, based
	on a Wilcoxon Rank Sum test and Welch's t-test (via aldex.ttest), a
	Kruskal-Wallis test (via aldex.kw), a generalized linear model (via
	aldex.glm), or a correlation test (via aldex.corr). All tests report
	p-values and Benjamini-Hochberg corrected p-values."""

	bioc = "ALDEx2"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ALDEx2_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ALDEx2/ALDEx2_1.34.0.tar.gz"]

	version("1.34.0", md5="359e47382b7cac1093aa1a5c24307cec", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/ALDEx2_1.34.0.tar.gz")

	depends_on("r-zcompositions", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))

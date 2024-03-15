# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetapod(RPackage):
	"""Meta-Analyses on P-Values of Differential Analyses.

	Implements a variety of methods for combining p-values in differential
	analyses of genome-scale datasets. Functions can combine p-values across
	different tests in the same analysis (e.g., genomic windows in ChIP-seq,
	exons in RNA-seq) or for corresponding tests across separate analyses
	(e.g., replicated comparisons, effect of different treatment conditions).
	Support is provided for handling log-transformed input p-values, missing
	values and weighting where appropriate."""

	bioc = "metapod"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metapod_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metapod/metapod_1.10.1.tar.gz"]

	version("1.10.1", md5="30dbb26bb39fae4345e0142e37fb2aa7")

	depends_on("r-rcpp", type=("build", "run"))

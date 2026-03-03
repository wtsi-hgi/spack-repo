# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarks(RPackage):
	"""Suffix Array Kernel Smoothing for discovery of correlative sequence motifs and multi-motif domains

	Suffix Array Kernel Smoothing (see https://academic.oup.com/bioinformatics/article-abstract/35/20/3944/5418797), or SArKS, identifies sequence motifs whose presence correlates with numeric scores (such as differential expression statistics) assigned to the sequences (such as gene promoters). SArKS smooths over sequence similarity, quantified by location within a suffix array based on the full set of input sequences. A second round of smoothing over spatial proximity within sequences reveals multi-motif domains. Discovered motifs can then be merged or extended based on adjacency within MMDs. False positive rates are estimated and controlled by permutation testing.
	"""
	
	homepage = "https://academic.oup.com/bioinformatics/article-abstract/35/20/3944/5418797"
	bioc = "sarks" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sarks_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sarks/sarks_1.14.0.tar.gz"]

	version("1.14.0", md5="b6fc7553269237bea782582b858aaee5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))

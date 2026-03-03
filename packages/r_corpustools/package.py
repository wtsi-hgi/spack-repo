# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorpustools(RPackage):
	"""Managing, Querying and Analyzing Tokenized Text

	Provides text analysis in R, focusing on the use of a tokenized text format. In this format, the positions of tokens are maintained, and each token can be annotated (e.g., part-of-speech tags, dependency relations).
    Prominent features include advanced Lucene-like querying for specific tokens or contexts (e.g., documents, sentences),
    similarity statistics for words and documents, exporting to DTM for compatibility with many text analysis packages,
    and the possibility to reconstruct original text from tokens to facilitate interpretation.
	"""
	
	homepage = "https://github.com/kasperwelbers/corpustools"
	cran = "corpustools" 

	version("0.5.1", md5="903cbcae989413d5e6fad80941e1c998")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wordcloud@2.5:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-udpipe@0.8.3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-quanteda@1.5.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tokenbrowser@0.1.5:", type=("build", "run"))
	depends_on("r-rnewsflow@1.2.1:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-pbapply@1.4:", type=("build", "run"))
	depends_on("r-rsyntax@0.1.1:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))

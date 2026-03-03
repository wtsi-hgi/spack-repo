# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextrank(RPackage):
	"""Summarize Text by Ranking Sentences and Finding Keywords

	The 'textrank' algorithm is an extension of the 'Pagerank' algorithm for text. The algorithm allows to summarize text by calculating how sentences are related to one another. This is done by looking at overlapping terminology used in sentences in order to set up links between sentences. The resulting sentence network is next plugged into the 'Pagerank' algorithm which identifies the most important sentences in your text and ranks them. 
    In a similar way 'textrank' can also be used to extract keywords. A word network is constructed by looking if words are following one another. On top of that network the 'Pagerank' algorithm is applied to extract relevant words after which relevant words which are following one another are combined to get keywords.  
    More information can be found in the paper from Mihalcea, Rada & Tarau, Paul (2004) <https://www.aclweb.org/anthology/W04-3252/>.
	"""
	
	homepage = "https://github.com/bnosac/textrank"
	cran = "textrank" 

	version("0.3.1", md5="b1eb76f52c62923fc112f172f098851e")

	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))

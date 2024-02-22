# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhocorasicktrie(RPackage):
	"""Fast Searching for Multiple Keywords in Multiple Texts

	Aho-Corasick is an optimal algorithm for finding many
    keywords in a text. It can locate all matches in a text in O(N+M) time; i.e.,
    the time needed scales linearly with the number of keywords (N) and the size of
    the text (M). Compare this to the naive approach which takes O(N*M) time to loop
    through each pattern and scan for it in the text. This implementation builds the
    trie (the generic name of the data structure) and runs the search in a single
    function call. If you want to search multiple texts with the same trie, the
    function will take a list or vector of texts and return a list of matches to
    each text. By default, all 128 ASCII characters are allowed in both the keywords
    and the text. A more efficient trie is possible if the alphabet size can be
    reduced. For example, DNA sequences use at most 19 distinct characters and
    usually only 4; protein sequences use at most 26 distinct characters and usually
    only 20. UTF-8 (Unicode) matching is not currently supported.
	"""
	
	homepage = "https://github.com/chambm/AhoCorasickTrie"
	cran = "AhoCorasickTrie" 

	version("0.1.2", md5="27615ea0e618f5478c9e491e4a2b7436")

	depends_on("r-rcpp", type=("build", "run"))

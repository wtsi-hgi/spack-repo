# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordAlignment(RPackage):
	"""Computing Word Alignment Using IBM Model 1 (and Symmetrization)
for a Given Parallel Corpus and Its Evaluation

	For a given Sentence-Aligned Parallel Corpus, it aligns words for each sentence pair. It considers one-to-many and symmetrization alignments. Moreover, it evaluates the quality of word alignment based on this package and some other software. It also builds an automatic dictionary of two languages based on given parallel corpus.
	"""
	
	cran = "word.alignment" 

	version("1.1", md5="1b6f7d7b31765e76ee3f1d1b78d2aaaa")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))

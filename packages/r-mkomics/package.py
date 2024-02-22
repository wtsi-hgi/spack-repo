# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkomics(RPackage):
	"""Omics Data Analysis

	Similarity plots based on correlation and median absolute deviation (MAD); adjusting colors for heatmaps; aggregate technical replicates; calculate pairwise fold-changes and log fold-changes; compute one- and two-way ANOVA; simplified interface to package 'limma' (Ritchie et al. (2015), <doi:10.1093/nar/gkv007> ) for moderated t-test and one-way ANOVA; Hamming and Levenshtein (edit) distance of strings as well as optimal alignment scores for global (Needleman-Wunsch) and local (Smith-Waterman) alignments with constant gap penalties (Merkl and Waack (2009), ISBN:978-3-527-32594-8).
	"""
	
	homepage = "https://www.stamats.de/"
	cran = "MKomics" 

	version("0.7", md5="4f149d4c0fe8b72add44a6d80e4dd921")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))

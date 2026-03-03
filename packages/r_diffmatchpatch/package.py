# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffmatchpatch(RPackage):
	"""String Diff, Match, and Patch Utilities

	A wrapper for Google's 'diff-match-patch' library. It provides basic tools
    for computing diffs, finding fuzzy matches, and constructing / applying patches to strings.
	"""
	
	homepage = "https://github.com/rundel/diffmatchpatch"
	cran = "diffmatchpatch" 

	version("0.1.0", md5="0969a7d1d718185c6de955bb21497ab9")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

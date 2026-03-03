# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdlibr(RPackage):
	"""R Integration for Edlib, the C/C++ Library for Exact Pairwise
Sequence Alignment using Edit (Levenshtein) Distance

	Bindings to edlib, a lightweight performant C/C++ library for exact pairwise sequence alignment using edit distance (Levenshtein distance). The algorithm computes the optimal alignment path, but also can be used to find only the start and/or end of the alignment path for convenience. Edlib was designed to be ultrafast and require little memory, with the capability to handle very large sequences. Three alignment methods are supported: global (Needleman-Wunsch), infix (Hybrid Wunsch), and prefix (Semi-Hybrid Wunsch). The original C/C++ library is described in "Edlib: a C/C++ library for fast, exact sequence alignment using edit distance", M. Šošić, M. Šikić, <doi:10.1093/bioinformatics/btw753>.
	"""
	
	homepage = "https://github.com/evanbiederstedt/edlibR"
	cran = "edlibR" 

	version("1.0.2", md5="5800fbd584a78f005e5702cc8ac6d89e")
	version("1.0.1", md5="f53fe2b1cacb5b614a5f4f54c5e7f93e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))

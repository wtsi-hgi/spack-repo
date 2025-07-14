# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRseqan(RPackage):
	"""R SeqAn

	Headers and some wrapper functions from the SeqAn C++ library for ease of usage in R.
	"""
	
	bioc = "RSeqAn"

	version("1.28.0", commit="e61edd0ee3f93a2599ba35a8d3856e6a934a919c")
	version("1.22.0", commit="79a530856d89a908c97f2e603ce4b4f62b99bd2f")

	depends_on("r-rcpp", type=("build", "run"))

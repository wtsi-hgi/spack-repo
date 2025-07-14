# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrMl(RPackage):
	"""Detecting patterns of post-transcriptional modifications using machine learning

	RNAmodR.ML extend the functionality of the RNAmodR package and classical detection strategies towards detection through machine learning models. RNAmodR.ML provides classes, functions and an example workflow to establish a detection stratedy, which can be packaged.
	"""
	
	homepage = "https://github.com/FelixErnst/RNAmodR.ML"
	bioc = "RNAmodR.ML"

	version("1.22.0", commit="4f3cd8971b40a4227ddaa7ad162d76783467f86c")
	version("1.16.0", commit="be466292ab3f430600489495b8f6a57d09dbdeb5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rnamodr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))

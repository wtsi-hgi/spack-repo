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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAmodR.ML_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAmodR.ML/RNAmodR.ML_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="b901fe7481a5080662886b51dd4015ac381ed96cf4b8ff8cd8bd5e8abe47a16d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rnamodr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummarizedbenchmark(RPackage):
	"""Classes and methods for performing benchmark comparisons

	This package defines the BenchDesign and SummarizedBenchmark classes for building, executing, and evaluating benchmark experiments of computational methods. The SummarizedBenchmark class extends the RangedSummarizedExperiment object, and is designed to provide infrastructure to store and compare the results of applying different methods to a shared data set. This class provides an integrated interface to store metadata such as method parameters and software versions as well as ground truths (when these are available) and evaluation metrics.
	"""
	
	homepage = "https://github.com/areyesq89/SummarizedBenchmark"
	bioc = "SummarizedBenchmark" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SummarizedBenchmark_2.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SummarizedBenchmark/SummarizedBenchmark_2.20.0.tar.gz"]

	version("2.20.0", sha256="0f04739892c4819d36787ee3f754ddb16a8360d72790c90c69cc99e3fca4ff99")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

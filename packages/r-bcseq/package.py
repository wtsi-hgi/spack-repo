# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcseq(RPackage):
	"""Fast Sequence Mapping in High-Throughput shRNA and CRISPR Screens

	This Rcpp-based package implements a highly efficient data structure and algorithm for performing alignment of short reads from CRISPR or shRNA screens to reference barcode library. Sequencing error are considered and matching qualities are evaluated based on Phred scores. A Bayes' classifier is employed to predict the originating barcode of a read. The package supports provision of user-defined probability models for evaluating matching qualities. The package also supports multi-threading.
	"""
	
	homepage = "https://github.com/jl354/bcSeq"
	bioc = "bcSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bcSeq_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bcSeq/bcSeq_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="338514ad92f5db3bcfecd825ef75a3fed1b503f2821ad3cc9c94236563821914")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))

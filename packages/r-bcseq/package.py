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

	version("1.30.0", commit="d62b2d789b48079f8bda5a0b549be1a907b672a5")
	version("1.24.0", commit="7dfa27ed35df2fa4bd92fb1aced6d9512bd34e39")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))

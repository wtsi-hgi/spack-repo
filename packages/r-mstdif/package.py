# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstdif(RPackage):
	"""A Collection of DIF Tests for Multistage Tests

	A collection of statistical tests for the detection of differential
    item functioning (DIF) in multistage tests. Methods entail logistic regression,
    an adaptation of the simultaneous item bias test (SIBTEST), and various score-based tests.
    The presented tests provide itemwise test for DIF along categorical, ordinal or metric covariates. Methods for uniform and non-uniform 
    DIF effects are available depending on which method is used.
	"""
	
	cran = "mstDIF" 

	version("0.1.7", md5="fc0fe2af61350063349ebb969d7cebc9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pp", type=("build", "run"))
	depends_on("r-mirt@1.31:", type=("build", "run"))
	depends_on("r-scdiftest", type=("build", "run"))
	depends_on("r-erm", type=("build", "run"))
